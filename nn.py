import telebot
import requests
import json
import re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton 
from telebot import types
tokenb = "5265076361:AAE6YB-PtXjrcPY94gBlOUSdCbMZdGk9p0c"
bot = telebot.TeleBot(tokenb)


# uplid ke peeyank bukan ke hadiok

@bot.message_handler(content_types=["text"])
def chatbot(message):
	teks = message.text
	if re.findall('buatbrand', teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=pisah&id="+teks
		page = requests.get(popo)
		koko = page.json()['data']['hasil']
		
		popo1 = 'https://cobaklik.link/botuser.php?pancer=buatbrand&id='+str(idd)+'&brand='+koko;
		page1 = requests.get(popo1)
		koko1 = page1.json()[0]['status']
		ket = page1.json()[0]['ket']
		if koko == 'ook':
			bot.send_message(message.chat.id,'Anda Sukses Membuat Brand', reply_markup=markup_inline1())
		else:
			bot.send_message(message.chat.id,ket, reply_markup=markup_inline1())
	if re.findall('ganti wa#', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id,'ok ganti wa', reply_markup=markup_inline1())
	if re.findall('/start', teks):
		bot.delete_message(message.chat.id, message.message_id)
		pesan = 'Menu Utama => akses menu utama ketik /menu'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())
	if re.findall('/menu', teks):
		bot.delete_message(message.chat.id, message.message_id)
		pesan = 'Menu Utama => akses menu utama ketik /menu'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())
	if re.findall('✅ ten',teks):
		simbol = 'ten'
		bot.delete_message(message.chat.id, message.message_id)
		base_url = "https://www.indodax.com"
		api_url = base_url+"/api/ticker/"+simbol+"idr";
		page = requests.get(api_url)
		koko = page.json().get("ticker").get("last")
		popo = 'https://cobaklik.link/hargacoin.php?id='+str(koko)
		page2 = requests.get(popo)
		harfa = page2.json().get("data").get("hasil")
		bot.send_message(message.chat.id, "Harga "+simbol+'\n\nHarga '+simbol+' Saat'+
		' Ini Adalah Rp '+harfa)
	if re.findall('✅ doge',teks):
		simbol = 'doge'
		bot.delete_message(message.chat.id, message.message_id)
		base_url = "https://www.indodax.com"
		api_url = base_url+"/api/ticker/"+simbol+"idr";
		page = requests.get(api_url)
		koko = page.json().get("ticker").get("last")
		popo = 'https://cobaklik.link/hargacoin.php?id='+str(koko)
		page2 = requests.get(popo)
		harfa = page2.json().get("data").get("hasil")
		bot.send_message(message.chat.id, "Harga "+simbol+'\n\nHarga '+simbol+' Saat'+
		' Ini Adalah Rp '+harfa)
	if re.findall('✅ aave',teks):
		simbol = 'aave'
		bot.delete_message(message.chat.id, message.message_id)
		base_url = "https://www.indodax.com"
		api_url = base_url+"/api/ticker/"+simbol+"idr";
		page = requests.get(api_url)
		koko = page.json().get("ticker").get("last")
		popo = 'https://cobaklik.link/hargacoin.php?id='+str(koko)
		page2 = requests.get(popo)
		harfa = page2.json().get("data").get("hasil")
		bot.send_message(message.chat.id, "Harga "+simbol+'\n\nHarga '+simbol+' Saat'+
		' Ini Adalah Rp '+harfa)
	if re.findall('✅ xrp',teks):
		simbol = 'xrp'
		bot.delete_message(message.chat.id, message.message_id)
		base_url = "https://www.indodax.com"
		api_url = base_url+"/api/ticker/"+simbol+"idr";
		page = requests.get(api_url)
		koko = page.json().get("ticker").get("last")
		popo = 'https://cobaklik.link/hargacoin.php?id='+str(koko)
		page2 = requests.get(popo)
		harfa = page2.json().get("data").get("hasil")
		bot.send_message(message.chat.id, "Harga "+simbol+'\n\nHarga '+simbol+' Saat'+
		' Ini Adalah Rp '+harfa)
	if re.findall('✅ eth',teks):
		simbol = 'eth'
		bot.delete_message(message.chat.id, message.message_id)
		base_url = "https://www.indodax.com"
		api_url = base_url+"/api/ticker/"+simbol+"idr";
		page = requests.get(api_url)
		koko = page.json().get("ticker").get("last")
		popo = 'https://cobaklik.link/hargacoin.php?id='+str(koko)
		page2 = requests.get(popo)
		harfa = page2.json().get("data").get("hasil")
		bot.send_message(message.chat.id, "Harga "+simbol+'\n\nHarga '+simbol+' Saat'+
		' Ini Adalah Rp '+harfa)
	if re.findall('✅ btc',teks):
		simbol = 'btc'
		bot.delete_message(message.chat.id, message.message_id)
		base_url = "https://www.indodax.com"
		api_url = base_url+"/api/ticker/"+simbol+"idr";
		page = requests.get(api_url)
		koko = page.json().get("ticker").get("last")
		popo = 'https://cobaklik.link/hargacoin.php?id='+str(koko)
		page2 = requests.get(popo)
		harfa = page2.json().get("data").get("hasil")
		bot.send_message(message.chat.id, "Harga "+simbol+'\n\nHarga '+simbol+' Saat'+
		' Ini Adalah Rp '+harfa)
	if re.findall('🚹 Profile',teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=profil&id="+ str(idd)
		page = requests.get(popo)
		paket = page.json()[0]['paket']
		tanggalberakhir = page.json()[0]['tanggalberakhir']
		nama = page.json()[0]['nama']
		mama ='»» Profil ««\n\n🆔 ID Pengguna : '+str(idd)+'\n💎 Nama Brand : '+nama+'\n🧰 Paket : '+paket+'\n📬 Link Dibuat\n📭 Total Link Tersedia\n📆 Akhir Paket : '+tanggalberakhir+'\nℹ️ bot coba klik link\n'
		bot.send_message(message.chat.id, mama)
	if re.findall('💠 Harga Coin', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Silahkan Pilih Coin", reply_markup=harga1())
	if re.findall('️️ Kembali', teks):
		bot.delete_message(message.chat.id, message.message_id)
		pesan = 'Menu Utama => akses menu utama ketik /menu'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())
	if re.findall('🌐 Smart Contract', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Smart Contract\n0x09929382983287823872837283238")
	if re.findall('🛅 Buat Link', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Masih Diperbaiki")
	if re.findall('🛗 Link WA', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Masih Diperbaiki")
	if re.findall('🛄 Semua Link', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Masih Diperbaiki")
	if re.findall('♻️ Bantuan', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id,"Silahkan Pilih Salah Satu Kontak Dibawah ini", reply_markup=bantuan())









 # jika menggunakan button
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	if call.data == "buatbrand":
		bot.delete_message(call.message.chat.id, call.message.message_id)
		pesan = 'Membuat Brand\n\nbrand berfungsi menjadi id link anda\nmisal brand anda bernama "koko"\nmaka, link yang didapatkan adalah\n1. Untuk Menuju ke chat whatsapp akan mendaparkan "cobaklik.link/koko"\n2. Untuk Link produk akan mendapatkan "cobaklik.link/koko-linkanda" dan linkanda bisa di custom sesuai keinginan\n\nCara Membuat Brand:\ncaranya adalah \nketik : buatbrandnamabrand\nnama brand ganti dengan nama brand yang ingin anda buat\nlalu kirimkan'
		bot.send_message(call.message.chat.id, pesan, reply_markup=markup_inline1())
 # jika menggunakan button
		
		
		
def harga1():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("✅ btc")
	b =  types.KeyboardButton("✅ eth")
	c =  types.KeyboardButton("✅ xrp")
	d =  types.KeyboardButton("✅ aave")
	e =  types.KeyboardButton("✅ doge")
	f =  types.KeyboardButton("✅ ten")
	g =  types.KeyboardButton("◀️️ Kembali")
	markup.ResizeKeyboard = True
	markup.row(a,b,c)
	markup.row(d,e,f)
	markup.row(g)
	return markup
	
def brandkosong1():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("💠 Harga Coin")
	b =  types.KeyboardButton("🛅 Buat Brand")
	c =  types.KeyboardButton("🌐 Smart Contract")
	g =  types.KeyboardButton("♻️ Bantuan")
	h =  types.KeyboardButton("🆎 About")
	markup.height = 1
	markup.row(a)
	markup.row(b)
	markup.row(c)
	markup.row(g,h)
	return markup
	
def awak():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("💠 Harga Coin")
	b =  types.KeyboardButton("🚹 Profile")
	c =  types.KeyboardButton("🛄 Semua Link")
	d =  types.KeyboardButton("🛗 Link WA")
	e =  types.KeyboardButton("🛅 Buat Link")
	f =  types.KeyboardButton("🌐 Smart Contract")
	g =  types.KeyboardButton("♻️ Bantuan")
	h =  types.KeyboardButton("🆎 About")
	
	markup.height = 1
	markup.width = 1
	markup.row(a)
	markup.row(b,c)
	markup.row(d,e)
	markup.row(f)
	markup.row(g,h)
	return markup
	
#button
def brandkosong():
	markup = InlineKeyboardMarkup()
	markup.width = 4
	markup.add(
		InlineKeyboardButton("💠 Harga Coin", callback_data = "HargaCoin")
	)
	markup.add(
		InlineKeyboardButton("🛅 Buat Brand", callback_data = "buatbrand")
	)
	markup.add(
		InlineKeyboardButton("🌐 Smart Contract", callback_data = "SmartContract")
	)
	return markup
	
def bantuan():
	markup = InlineKeyboardMarkup()
	markup.width = 4
	markup.add(
		InlineKeyboardButton("Whatsapp", "cobaklik.link/Hadi"),
		InlineKeyboardButton("Telegram",  "https://t.me/peeyank")
	)
	return markup

def markup_inline1():
	markup = InlineKeyboardMarkup()
	markup.width = 4
	markup.add(
		InlineKeyboardButton("Ke Menu Utama", callback_data = "Kembali")
	)
	return markup
	
def markup_inline():
	markup = InlineKeyboardMarkup()
	markup.width = 4
	markup.add(
		InlineKeyboardButton("💠 Harga Coin", callback_data = "HargaCoin")
	)
	markup.add(
		InlineKeyboardButton("🚹 Profile", callback_data = "Profile"),
		InlineKeyboardButton("🛄 Semua Link", callback_data = "SemuaLink")
	)
	markup.add(
		InlineKeyboardButton("🛗 Link WA", callback_data = "LinkWA"),
		InlineKeyboardButton("🛅 Buat Link", callback_data = "BuatLink")
	)
	markup.add(
		InlineKeyboardButton("🌐 Smart Contract", callback_data = "SmartContract")
	)
	return markup
	
def harga():
	markup = InlineKeyboardMarkup()
	markup.width = 4
	markup.add(
		InlineKeyboardButton("Btc", callback_data = "btc"),
		InlineKeyboardButton("Eth", callback_data = "eth"),
		InlineKeyboardButton("Xrp", callback_data = "xrp")
	)
	markup.add(
		InlineKeyboardButton("Aave", callback_data = "aave"),
		InlineKeyboardButton("Doge", callback_data = "doge"),
		InlineKeyboardButton("Ten", callback_data = "ten")
	)
	markup.add(
		InlineKeyboardButton("Ke Menu Utama", callback_data = "Kembali")
	)
	return markup
	
print('bot berjalan')
bot.polling()
