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
		if ket == 'ook':
			bot.send_message(message.chat.id,'Anda Sukses Membuat Brand', reply_markup=awak())
		else:
			bot.send_message(message.chat.id,ket)
	if re.findall('Buatbrand', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id,'Harus Huruf Kecil Semua\nbuatbrand\nlalu tambahkan brand anda\nContoh\nbuatbrandhadiok')
	if re.findall('Gantiwa', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id,'Harus Huruf Kecil Semua\ngantiwa\nlalu tambahkan nomor whatsapp anda\nContoh\ngantiwa089xxxxxx')
	
	if re.findall('gantiwa', teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=pisah2&id="+teks
		page = requests.get(popo)
		nomorwa = page.json()['data']['hasil']

		popo1 = "https://cobaklik.link/botuser.php?pancer=gantiwanya&id="+str(idd)+'&nomorwa='+str(nomorwa)
		page1 = requests.get(popo1)
		status = page1.json()['data']['status']
		ket = page1.json()['data']['ket']

		if status == 'true':
			bot.send_message(message.chat.id,'>>Sukses<<\n\nAnda Sukses Mengganti Nomor Whatsapp')
		else:
			bot.send_message(message.chat.id,'>>Gagal<<\n\n'+ket)
		

	if re.findall('/start', teks):
		bot.delete_message(message.chat.id, message.message_id)
		pesan = 'Menu Utama => akses menu utama ketik /menu'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		popo1 = "https://cobaklik.link/botuser.php?pancer=logbot&id="+ str(idd)+'&log=start'
		page1 = requests.get(popo1)
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
		popo1 = "https://cobaklik.link/botuser.php?pancer=logbot&id="+ str(idd)+'&log=menu'
		page1 = requests.get(popo1)
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

	if re.findall('🧑‍🎤 Profile',teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=profil&id="+ str(idd)
		page = requests.get(popo)
		link = page.json()[0]['link']
		linktersedia = page.json()[0]['piket']
		paket = page.json()[0]['paket']
		tanggalberakhir = page.json()[0]['tanggalberakhir']
		nama = page.json()[0]['nama']
		mama ='»» Profil ««\n\n🆔 ID Pengguna : '+str(idd)+'\n💎 Nama Brand : '+nama+'\n🧰 Paket : '+paket+'\n📬 Link Dibuat : '+str(link)+'\n📭 Total Link Tersedia : '+str(linktersedia)+'\n📆 Akhir Paket : '+tanggalberakhir+'\nℹ️ bot coba klik link\n'
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
		popo1 = "https://cobaklik.link/botuser.php?pancer=logbot&id="+ str(idd)+'&log=start'
		page1 = requests.get(popo1)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())
	if re.findall('🌐 Smart Contract', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Smart Contract\n0x09929382983287823872837283238")
	if re.findall('🔗 Buat Link', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Masih Diperbaiki")

	if re.findall('❇️ Link WA', teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=linkwa&id="+ str(idd)
		page = requests.get(popo)

		popo1 = "https://cobaklik.link/botuser.php?pancer=ambilnomorwa&id="+ str(idd)
		page1 = requests.get(popo1)
		
		linkwa = page.json()[0]['pendek']
		nomorwa = page1.json()['data']['ket']
		mama ='»» Link Whatsapp Kamu ««\n\n# Ini Nomor Whatsapp Kamu\n📞 '+nomorwa+'\n\n# ini Link Whatsapp Kamu\n⛓ cobaklik.link/'+linkwa+'\n\n🎁 Jika link diatas di klik, akan langsung menuju ke nomor whatsapp kamu\n\n⚠ Untuk Mengganti Nomor Whatsapp Tujuan Silahkan Klik Tombol Dibawah..'
		bot.send_message(message.chat.id, mama,reply_markup=gantinomorwa())

	if re.findall('🛄 Semua Link', teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=semualink&id="+ str(idd)
		page = requests.get(popo)
		mama ='»» Semua Link Yank Kamu Punya ««\n\n'
		bot.send_message(message.chat.id, mama)
		aa = page.json()
		asa = 0

		markup = InlineKeyboardMarkup()
		markup.width = 4

		for c in aa: 
			asa = asa + 1
			bot.send_message(message.chat.id, str(asa) + '. cobaklik.link/' + c['as'], reply_markup=markup)

	if re.findall('♻️ Bantuan', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id,"Silahkan Pilih Salah Satu Kontak Dibawah ini", reply_markup=bantuan())
	if re.findall('🆎 About', teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo1 = "https://cobaklik.link/botuser.php?pancer=logbot&id="+ str(idd)+'&log=about'
		page1 = requests.get(popo1)

		markup = types.ReplyKeyboardMarkup()
		a =  types.KeyboardButton("💠 Harga Coin")
		b =  types.KeyboardButton("◀️️ Kembali")
		markup.resize_keyboard = True
		markup.one_time_keyboard = False
		markup.row(b,a)
		bot.send_message(message.chat.id, "Silahkan Cek Harga Coin Dengan Menekan Tombol di Bawah",reply_markup=markup)

	if re.findall('🛅 Buat Brand', teks):
		bot.delete_message(message.chat.id, message.message_id)
		pesan = 'Membuat Brand\n\nbrand berfungsi menjadi id link anda\nmisal brand anda bernama "koko"\nmaka, link yang didapatkan adalah\n1. Untuk Menuju ke chat whatsapp akan mendaparkan "cobaklik*link/koko"\n2. Untuk Link produk akan mendapatkan "cobaklik*link/koko-linkanda" dan linkanda bisa di custom sesuai keinginans'
		bot.send_message(message.chat.id, pesan,reply_markup=tombolbuatbrand())
	
	if re.findall('✅ Ganti Nomor Whatsapp', teks):
		bot.delete_message(message.chat.id, message.message_id)
		pesan = '>>Cara Ganti Nomor Whatsapp<<\n\nketik:\ngantiwa089646509977\ngantiwa dan nomor hp digabung tanpa ada spasi'
		bot.send_message(message.chat.id, pesan)
	
	if re.findall('📬 Paket', teks):
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(message.chat.id, "Masih Diperbaiki")

	if re.findall('💠 Masukkan Brand Anda', teks):
		bot.delete_message(message.chat.id, message.message_id)
		idd = message.from_user.id
		popo1 = "https://cobaklik.link/botuser.php?pancer=logbot&id="+ str(idd)+'&log=buatbrand'
		page1 = requests.get(popo1)
		bot.send_message(message.chat.id,"Silahkan Masukkan Nama Brand Anda")

	else:
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?pancer=ambillogbot&id="+ str(idd)
		page = requests.get(popo)
		status = page.json()['data']['status']
		if status == 'buatbrand':
			bot.send_message(message.chat.id, 'Nama Brand Yang Kamu Pilih : '+teks+'\nSilahkan Tunggu....')
			idd = message.from_user.id
			popo1 = 'https://cobaklik.link/botuser.php?pancer=buatbrand&id='+str(idd)+'&brand='+teks;
			page1 = requests.get(popo1)
			koko1 = page1.json()[0]['status']
			ket = page1.json()[0]['ket']
			if ket == 'ook':
				bot.delete_message(message.chat.id, message.message_id)
				idd = message.from_user.id
				popo1 = "https://cobaklik.link/botuser.php?pancer=logbot&id="+ str(idd)+'&log=start'
				page1 = requests.get(popo1)
				bot.send_message(message.chat.id,'Anda Sukses Membuat Brand',reply_markup=awak())
			else:
				bot.delete_message(message.chat.id, message.message_id)
				bot.send_message(message.chat.id,ket+'\nSilahkan Masukkan Brand Anda Lagi, Atau Klik Kembali',reply_markup=tombolbuatbrand())












 # jika menggunakan button
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	if call.data == "buatbrand":
		bot.delete_message(call.message.chat.id, call.message.message_id)
		pesan = 'Membuat Brand\n\nbrand berfungsi menjadi id link anda\nmisal brand anda bernama "koko"\nmaka, link yang didapatkan adalah\n1. Untuk Menuju ke chat whatsapp akan mendaparkan "cobaklik.link/koko"\n2. Untuk Link produk akan mendapatkan "cobaklik.link/koko-linkanda" dan linkanda bisa di custom sesuai keinginan\n\nCara Membuat Brand:\ncaranya adalah \nketik : buatbrandnamabrand\nnama brand ganti dengan nama brand yang ingin anda buat\nlalu kirimkan'
		bot.send_message(call.message.chat.id, pesan, reply_markup=markup_inline1())
	if call.data == "CaraBuatBrand":
		bot.delete_message(call.message.chat.id, call.message.message_id)
		pesan = 'Cara Membuat Brand:\ncaranya adalah \nketik : buatbrandnamabrand\nnama brand ganti dengan nama brand yang ingin anda buat\nlalu kirimkan'
		bot.send_message(call.message.chat.id, pesan)
 # jika menggunakan button
		


def tombolbuatbrand():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("💠 Masukkan Brand Anda")
	b =  types.KeyboardButton("◀️️ Kembali")
	markup.resize_keyboard = True
	markup.one_time_keyboard = False
	markup.row(b,a)
	return markup



def gantinomorwa():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("✅ Ganti Nomor Whatsapp")
	b =  types.KeyboardButton("◀️️ Kembali")
	markup.resize_keyboard = True
	markup.one_time_keyboard = False
	markup.row(b,a)
	return markup
		
		
def harga1():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("✅ btc")
	b =  types.KeyboardButton("✅ eth")
	c =  types.KeyboardButton("✅ xrp")
	d =  types.KeyboardButton("✅ aave")
	e =  types.KeyboardButton("✅ doge")
	f =  types.KeyboardButton("✅ ten")
	g =  types.KeyboardButton("◀️️ Kembali")
	h =  types.KeyboardButton("🌐 Smart Contract")
	markup.resize_keyboard = True
	markup.one_time_keyboard = False
	markup.row(a,b,c)
	markup.row(d,e,f)
	markup.row(g,h)
	return markup
	
def brandkosong1():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("🛅 Buat Brand")
	b =  types.KeyboardButton("🧑‍🎤 Profile")
	c =  types.KeyboardButton("🛄 Semua Link")
	d =  types.KeyboardButton("❇️ Link WA")
	e =  types.KeyboardButton("🔗 Buat Link")
	g =  types.KeyboardButton("♻️ Bantuan")
	h =  types.KeyboardButton("🆎 About")
	i =  types.KeyboardButton("📬 Paket")
	j =  types.KeyboardButton("📶 Statistik")
	markup.resize_keyboard = True
	markup.one_time_keyboard = False
	
	markup.height = 1
	markup.width = 1
	markup.row(b,c,d)
	markup.row(e,i,j)
	markup.row(a,g,h)
	return markup
	
def awak():
	markup = types.ReplyKeyboardMarkup()
	a =  types.KeyboardButton("🛅 Buat Brand")
	b =  types.KeyboardButton("🧑‍🎤 Profile")
	c =  types.KeyboardButton("🛄 Semua Link")
	d =  types.KeyboardButton("❇️ Link WA")
	e =  types.KeyboardButton("🔗 Buat Link")
	g =  types.KeyboardButton("♻️ Bantuan")
	h =  types.KeyboardButton("🆎 About")
	i =  types.KeyboardButton("📬 Paket")
	j =  types.KeyboardButton("📶 Statistik")
	markup.resize_keyboard = True
	markup.one_time_keyboard = False
	
	markup.height = 1
	markup.width = 1
	markup.row(b,c,d)
	markup.row(e,i,j)
	markup.row(a,g,h)
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

def carabuatbrandok():
	markup = InlineKeyboardMarkup()
	markup.width = 4
	markup.add(
		InlineKeyboardButton("✅ Cara Buat Brand", callback_data = "CaraBuatBrand")
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


# buat file Procfile isinya bot: python mm.py
# ketik command pip freeze > requitements.txt

# heroku login
# git init
# git add .
# heroku create
# git commit -m "awalnya1"
# git push heroku master
# heroku ps:scale bot=1





# push github
# ----------------------------------------------------------------

# git config --global user.name "peeyanku"
# git config --global user.email "emailrelevan@gmail.com"
# git init
# git add .
# git commit -m "awalnya1"
# git remote add origin git@github.com:peeyanku/kok.git


# git push -u origin master
