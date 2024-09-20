#!/usr/bin/env python3
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.filters import command, regex

from bot import bot, LOGGER, OWNER_ID, config_dict
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage, auto_delete_message
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.ext_utils.bot_utils import sync_to_async, new_task, is_gdrive_link, get_readable_file_size


@new_task
async def driveclean(_, message):
    args = message.text.split()
    if len(args) > 1:
        link = args[1].strip()
    elif reply_to := message.reply_to_message:
        link = reply_to.text.split(maxsplit=1)[0].strip()
    else:
        link = f"https://drive.google.com/drive/folders/{config_dict['GDRIVE_ID']}"
    if not is_gdrive_link(link):
        return await sendMessage(message, 'No GDrive Link Provided')
    clean_msg = await sendMessage(message, '<i>Fetching ...</i>')
    gd = GoogleDriveHelper()
    name, mime_type, size, files, folders = await sync_to_async(gd.count, link)
    try:
        drive_id = GoogleDriveHelper.getIdFromUrl(link)
    except (KeyError, IndexError):
        return await editMessage(clean_msg, "Google Drive ID could not be found in the provided link")
    buttons = ButtonMaker()
    buttons.ibutton('Pindah ke Sampah', f'gdclean clear {drive_id} trash')
    buttons.ibutton('Hapus Permanen', f'gdclean clear {drive_id}')
    buttons.ibutton('Berhenti Pembersihan', 'gdclean stop', 'footer')
    await editMessage(clean_msg, f'''⌬ <b><i>GDrive Clean/Trash :</i></b>
    
🔴<b>Name Folder  :</b> {name}
🔴<b>Ukuran Folder :</b> {get_readable_file_size(size)}
🔴<b>Jumlah Files   :</b> {files}
🔴<b>Jumlah Folder :</b> {folders}
    
<b>NOTES:</b>
<i>1. Semua file terhapus permanen jika Del Permanen, tidak dipindahkan ke sampah.
2. Folder tidak terhapus.
3. Hapus file folder khusus melalui pemberian tautan bersama dengan cmd, tetapi harus memiliki izin penghapusan.
4. Pindah ke Bin Memindahkan semua file Anda ke sampah tetapi dapat dikembalikan lagi jika memiliki izin.</i>
    
<code>Pilih Tindakan yang Diperlukan di bawah ini untuk Membersihkan Drive Anda!</code>''', buttons.build_menu(2))


@new_task
async def drivecleancb(_, query):
    message = query.message
    user_id = query.from_user.id
    data = query.data.split()
    if user_id != OWNER_ID:
        await query.answer(text="Not Owner!", show_alert=True)
        return
    if data[1] == "clear":
        await query.answer()
        await editMessage(message, '<i>Processing Drive Clean / Trash...</i>')
        drive = GoogleDriveHelper()
        msg = await sync_to_async(drive.driveclean, data[2], trash=len(data)==4)
        await editMessage(message, msg)
    elif data[1] == "stop":
        await query.answer()
        await editMessage(message, '⌬ <b>Pembersihan GDrive di batalkan</b>')
        await auto_delete_message(message, message)
        

bot.add_handler(MessageHandler(driveclean, filters=command(BotCommands.GDCleanCommand) & CustomFilters.owner))
bot.add_handler(CallbackQueryHandler(drivecleancb, filters=regex(r'^gdclean')))