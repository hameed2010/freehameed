import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    import time
    import datetime
except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    import datetime 
    import requests 
   
    pass

from keep_alive import keep_alive
keep_alive()



db = uu('dbs/hameeed.ss', 'rshq')\

print(db)
ALLOWED_GROUP_ID = -1002286207232 
mor_button = btn("📁طلب المزيد 📁", url=f'https://t.me/eitabbbb')
channel_button = btn("📢 قناه الخدمة 📢", url=f'https://t.me/freepikprem1')
calladmin = mk().add(mor_button).add(channel_button)
bot = TeleBot(token="7536129194:AAH7xiyzsadwEKvNXskin3Oo1Yjycq4JNNA")
MAX_MESSAGES_PER_DAY = 1
admin = 6698161283 
bk = mk(row_width=1).add(btn('رجوع', callback_data='back'))
with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

def extract_freepik_id(url):
    match = re.search(r'_(\d+)\.htm', url)
    if match:
        return match.group(1)
    return None
 # إذا لم يتم العثور على رقم
stypes = ['member', 'administrator', 'creator']
if not db.get('accounts'):
    db.set('accounts', [])
    pass

if not db.get("admins"):
    db.set('admins', [admin, ])
if not db.get('badguys'):
    db.set('badguys', [])

if not db.get('force'):
    db.set('force', [])
if not db.get('subscription'):
    db.set('subscription', [])    
if not db.get('token_table'):
    db.set('token_table', [])   
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        print(x)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    
  
    keys = mk(row_width=2)
    if user_id in db.get("admins") :
        keys_ = mk()
        btn01 = btn('🤍الاحصائيات', callback_data='stats')
        btn02 = btn("⚠️اذاعة", callback_data='cast')
        btn05, btn06 = btn('➖حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
       
        btna = btn('➕تفعيل ViP', callback_data='addsubscription')
        btnl = btn('➖الغاء ViP', callback_data='delsubscription')
        leave = btn('➖   معرفه المتبقي من الاشتراك ', callback_data='checksubscription')
        
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        
        btn03 = btn('➕اضافة ادمن', callback_data='addadmin')
        btn04 = btn('➖مسح ادمن', callback_data='deladmin')

        btn012 = btn('⚠️الادمنية ', callback_data='admins')
        btn013 = btn(' المشتركين', callback_data='subscription')
        btn014 = btn(' التوكن', callback_data='token_function')
        btn015 = btn(' التوكن الموجود', callback_data='show_all_tokens')
        keys_.add(btn03, btn04)
        keys_.add(btn012, btn11)
        
         
        
        keys_.add(btna, btnl)
        keys_.add(btn013)
        keys_.add(leave)
        keys_.add(btn014,btn015)
      
        bot.reply_to(message, messages['admin_panel_message'], reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                    check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                    keyboard = mk().add(channel_button).add(check_button)
                    bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        
        
        
        
        return bot.reply_to(message, messages['welcome_message'])
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                keyboard = mk().add(channel_button).add(check_button)
                bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                return
    
    
   
   

    return bot.reply_to(message,messages['welcome_message'])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_id in db.get('badguys'): return
    
    chat_id = message.chat.id
    if chat_id != ALLOWED_GROUP_ID and chat_id != user_id:
        bot.reply_to(message, "عذرًا، أنا أعمل فقط في مجموعة @freepikprem1  معينة أو في البوت نفسه.")
        return
        bot.reply_to(message, "عذرًا، أنا أعمل فقط في مجموعة معينة.")
        return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                    check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                    keyboard = mk().add(channel_button).add(check_button)
                    bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@" + channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                keyboard = mk().add(channel_button).add(check_button)
                bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                return

    # جلب بيانات الاشتراك من القائمة
    download_resource( message,user_id,message.message_id,message.chat.id)
def download_resource( message, user_id,midw,chatid):
    # جلب بيانات المستخدم
    user_messages = db.get(f"{user_id}_messages") or {}
    today = datetime.date.today()
    messages_today = user_messages.get(str(today), 0)
    print(user_id)
    
    # جلب بيانات الاشتراك للمستخدم
    subscriptions = db.get('subscriptions') or []
    sub_data = None
    for sub in subscriptions:
        if sub['user_id'] == user_id:
            sub_data = sub
            break

    # تحديد الحد الأقصى للتنزيلات اليومية بناءً على حالة الاشتراك
    if sub_data:
        max_downloads = sub_data.get("max_downloads_per_day", MAX_MESSAGES_PER_DAY)
    else:
        max_downloads = MAX_MESSAGES_PER_DAY  # غير مشترك: حد يومي واحد فقط

    # التحقق مما إذا كان المستخدم قد بلغ الحد الأقصى للتنزيلات اليومية
    if messages_today >= max_downloads:
        user_name = message.from_user.first_name or "عزيزي المستخدم"
        message_text = f"""
<b>مرحبا {user_name}</b>
لقد بلغت الحد الأقصى لعدد التحميلات اليومية 
<b><blockquote>نأسف، لقد تم منعك من الإرسال.</blockquote></b>

<b>لإتمام طلب المزيد من الملفات، يتطلب الأمر الاشتراك:</b>
- تحدث مع أحد المشرفين.
- <a href="https://t.me/eitabbbb">اضغط هنا للإشتراك</a>.

شكرًا على تفهمك!
"حاول مرة أخرى غدًا.
"""
        bot.reply_to(message,message_text, parse_mode="HTML" ,reply_markup=calladmin)
        return False

    # استخراج ID المورد من الرابط
    
    resource_id = extract_freepik_id(message.text)
    if resource_id is None:
        bot.reply_to(message, messages['invalid_link_message'])
        return False
    
    # بدء عملية التنزيل
    

    # تنزيل المورد باستخدام API
    token_data = db.get('token_table')
    tokens_string = ", ".join(map(str, token_data))
    url = f"https://api.freepik.com/v1/resources/{resource_id}/download"
    headers = {"x-freepik-api-key": tokens_string}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data_dict = json.loads(response.text)
        info = data_dict.get('data', {})
        filename = info.get('filename')
        file_url = info.get('url')

        if not filename or not file_url:
            print("❌ فشل في جلب بيانات الملف.")
            bot.reply_to(message, "❌ حدث خطأ أثناء تحميل الملف. يرجى المحاولة لاحقًا.")
            return False

        print(f"🔗 رابط الملف: {file_url}")
        user_messages[str(today)] = messages_today + 1
        remaining_downloads = max_downloads - (messages_today + 1)
        
        # إرسال الملف إلى المستخدم
        bot.send_document(chatid, file_url, midw,caption=f"📂 ملفك أصبح جاهز ✅ المتبقي لديك لتحميل ({max(0, remaining_downloads)}) لهذا اليوم.",reply_markup=calladmin)

        print(f"📤 تم إرسال الملف إلى المستخدم {user_id}")
        db.set(f"{user_id}_messages", user_messages)
        # تحديث عدد التنزيلات اليومية
        
        

        # حساب التنزيلات المتبقية
        
       

        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ خطأ أثناء التحميل: {e}")
        bot.reply_to(message, "❌ حدث خطأ أثناء تحميل الملف. يرجى المحاولة لاحقًا.")
        
        return False
    except Exception as e:
        print(f"⚠️ خطأ غير متوقع: {e}")
        mor_button = btn("  📁 تنزيل الملف 📁", url=f'{file_url}')
        channel_button = btn("📢 قناه الخدمة 📢", url=f'https://t.me/freepikprem1')
        calladmin = mk().add(mor_button).add(channel_button)
        bot.reply_to(message, f"📂 ملفك أصبح جاهز ✅ المتبقي لديك لتحميل ({max(0, remaining_downloads)}) لهذا اليوم.",reply_markup=calladmin)
        db.set(f"{user_id}_messages", user_messages)
        return False
@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    user_id = call.from_user.id
    cid, data, mid = call.from_user.id, call.data, call.message.id
    count_ord = db.get('orders') if db.get('orders') else 1
    if data == 'deladmin':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addadmin':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'token_function':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, token_function, type)
    if data == 'delsubscription':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من اشتراك',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)
    if data == 'addsubscription':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته اشتراك بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)   
    if data == 'checksubscription':
        type = 'check'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد معرفه اشتراك بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type) 
    if data == 'show_all_tokens':
        token_data = db.get('token_table')  # جلب جميع التوكنات

        if not token_data or token_data == []:
            bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
            return
        else:
            
            bot.edit_message_text(chat_id=cid, message_id=mid, text=token_data)

            return
             # تنسيق القائمة
             

    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
        

    if data == 'subscription':
        # جلب قائمة المشتركين من قاعدة البيانات
        subscriptions = db.get('subscriptions') or []

        if not subscriptions:
            bot.edit_message_text(chat_id=cid, message_id=mid, text="لا يوجد مشتركين بالبوت.")
            return

        # إعداد النص الذي سيعرض جميع المشتركين
        txt = "المشتركين:\n"
        today = datetime.date.today()

        for idx, sub in enumerate(subscriptions, 1):
            user_id = sub['user_id']
            end_date = sub['end_date']
            max_downloads = sub.get("max_downloads_per_day", "غير محدد")

            try:
                # محاولة الحصول على معلومات المستخدم (اسم المستخدم أو الاسم الأول)
                user_info = bot.get_chat(user_id)
                username = f"@{user_info.username}" if user_info.username else user_info.first_name
            except:
                username = f"ID: {user_id}"

            # جلب عدد التحميلات اليومية
            user_messages = db.get(f"{user_id}_messages") or {}
            messages_today = user_messages.get(str(today), 0)

            remaining_downloads = max_downloads - messages_today if max_downloads != "غير محدد" else "غير محدد"

            txt += f"{idx}. {username} - حتى {end_date} (عدد التحميلات اليومية: {max_downloads}, المتبقي: {remaining_downloads})\n"

        # عرض النص النهائي
        bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
    
    if data == 'check_subscription':
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@" + channel, user_id=user_id)
                if str(x.status) not in stypes:
                    bot.answer_callback_query(call.id, '❌ لا تزال غير مشترك، يرجى الاشتراك ثم إعادة المحاولة.')
                    return
        bot.answer_callback_query(call.id, '✅ تم التحقق من اشتراكك بنجاح!')
        bot.edit_message_text(' اهلاً بك في بوت التحميل من Freepik يرجى إرسال رابط الملف لتحميل✅  تم التحقق من اشتراكك، يمكنك الآن استخدام البوت.', chat_id=cid, message_id=mid)
    if data == 'banone':
        if cid in db.get("admins") :
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") :
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") :
            x  = bot.edit_message_text(text=f'ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    
    if data == 'setforce':

        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n@uf3_8 @uf3_8',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)

def set_user(id, data):
    db.set(f'user_{id}', data)
    return True
def setfo(message):
    if "@" not in message.text:
        bot.reply_to(message, f'• رجاء ارسل القناة بشكل صحيح')
        return 
    elif message.text == "/start":
        start_message(message)
        return 
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return

def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return
def subscription(message, action):
    try:
        user_id = int(message.text)
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إرسال **ID** المستخدم بشكل صحيح!")
        return

    if action == 'add':
        # طلب عدد الأيام من المسؤول
        msg = bot.reply_to(message, "يرجى إدخال عدد الأيام للاشتراك:")
        bot.register_next_step_handler(msg, process_days, user_id)

    elif action == 'delete':
        subscriptions = db.get('subscriptions') or []
        found = False

        # البحث عن المستخدم وإزالته من القائمة
        for sub in subscriptions:
            if sub['user_id'] == user_id:
                subscriptions.remove(sub)
                found = True
                break

        if found:
            db.set('subscriptions', subscriptions)
            bot.reply_to(message, f"❌ تم إلغاء اشتراك المستخدم **{user_id}** بنجاح.")
            bot.send_message('@freepikprem3', f"❌ تم إلغاء اشتراك المستخدم **{user_id}** بنجاح.")
        else:
            bot.reply_to(message, f"⚠️ لا يوجد اشتراك لهذا المستخدم.")

    elif action == 'check':
        subscriptions = db.get('subscriptions') or []
        found = False

        # البحث عن بيانات الاشتراك للمستخدم
        for sub in subscriptions:
            if sub['user_id'] == user_id:
                max_downloads = sub.get("max_downloads_per_day", "غير محدد")
                bot.reply_to(message, f"📅 اشتراك المستخدم **{user_id}** نشط حتى {sub['end_date']}.\n"
                                      f"عدد التحميلات اليومية: {max_downloads}.")
                found = True
                break

        if not found:
            bot.reply_to(message, f"⏳ لا يوجد اشتراك نشط لهذا المستخدم.")


def process_days(message, user_id):
    try:
        days = int(message.text)
        if days <= 0:
            raise ValueError
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إدخال عدد صحيح أكبر من صفر!")
        return

    # تحديد تاريخ البداية والنهاية بناءً على عدد الأيام
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=days)

    # طلب عدد التحميلات اليومية من المسؤول
    msg = bot.reply_to(message, "يرجى إدخال عدد التحميلات اليومية لهذا المشترك:")
    bot.register_next_step_handler(msg, process_max_downloads, user_id, start_date, end_date)


def process_max_downloads(message, user_id, start_date, end_date):
    try:
        max_downloads = int(message.text)
        if max_downloads <= 0:
            raise ValueError
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إدخال عدد صحيح أكبر من صفر!")
        return

    # جلب قائمة المشتركين الحالية أو إنشاء قائمة جديدة إذا كانت فارغة
    subscriptions = db.get('subscriptions') or []

    # إضافة بيانات الاشتراك الجديدة إلى القائمة
    subscriptions.append({
        "user_id": user_id,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "max_downloads_per_day": max_downloads
    })

    # حفظ القائمة المحدثة في قاعدة البيانات
    db.set('subscriptions', subscriptions)

    bot.reply_to(message, f"✅ تم تفعيل الاشتراك للمستخدم **{user_id}** حتى {end_date}.\n"
                          f"عدد التحميلات اليومية: {max_downloads}.")
    try:
        bot.send_message('@freepikprem3', f"✅ تم تفعيل الاشتراك للمستخدم **{user_id}** حتى {end_date}.\n"
                                          f"عدد التحميلات اليومية: {max_downloads}.")
        bot.send_message(user_id, f"🎉 تهانينا! تم تفعيل اشتراكك حتى {end_date}.\n"
                                  f"يمكنك الآن تحميل {max_downloads} ملفات يوميًا. ✅")
    except Exception as e:
        print(f"⚠️ فشل إرسال الرسالة للمستخدم {user_id}: {e}")
        
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return
def token_function(message, type):
    user_id = message.text  # السماح بأي نص وإزالة المسافات الزائدة

    if type == 'add':
        db.set('token_table', [user_id])  # استبدال التوكن الحالي بالتوكن الجديد
        bot.reply_to(message, f'• تم تعيين التوكن الجديد بنجاح ✅\n• التوكن: {user_id}')

    elif type == 'delete':
        token_data = db.get('token_table') or []  # جلب التوكن الحالي
        if user_id not in token_data:
            bot.reply_to(message, '• هذا التوكن غير موجود')
        else:
            db.set('token_table', [])  # إزالة التوكن
            bot.reply_to(message, '• تم ازالة التوكن بنجاح ✅')
def casting(message):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الي مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الي : {bad} ')
    return

try:
    bot.infinity_polling()
except:
    pass   
