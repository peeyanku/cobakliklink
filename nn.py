import telebot
import requests
import mysql.connector
import random
import json
import re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton 
from telebot import types
tokenb = "5134173195:AAGmd-BSLiuPGBl_Qpuq_L9JToqxwG2T5_A"
bot = telebot.TeleBot(tokenb)

keamanan = 0


@bot.message_handler(content_types=["text"])
def chatbot(message):
	pancerbatal=''
	teks = message.text
	if re.findall('buatbrand', teks):
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=pisah&id="+teks
		page = requests.get(popo)
		koko = page.json()['data']['hasil']
		
		popo1 = 'https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=buatbrand&id='+str(idd)+'&brand='+koko;
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
	

	if re.findall('/start', teks):
		pesan = 'Ini adalah layanan pemendek link\nAnda bisa mendapatkan link untuk menuju ke whatsapp anda\nDisini juga bisa membuat link pendek untuk menuju link produk anda.\nSilahkan Explore menu untuk mendapatkan fiture menariknya.'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=start'
		page1 = requests.get(popo1)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())

	if re.findall('/menu', teks):
		pesan = 'Ini adalah layanan pemendek link\nAnda bisa mendapatkan link untuk menuju ke whatsapp anda\nDisini juga bisa membuat link pendek untuk menuju link produk anda.\nSilahkan Explore menu untuk mendapatkan fiture menariknya.'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=menu'
		page1 = requests.get(popo1)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())


	if re.findall('️️ Kembali', teks):
		pesan = 'Menu Utama => akses menu utama ketik /menu'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=start'
		page1 = requests.get(popo1)
		koko = page.json()['data']['status']
		if koko == 'brand kosong':
			bot.send_message(message.chat.id,pesan, reply_markup=brandkosong1())
		else:
			bot.send_message(message.chat.id,pesan, reply_markup=awak())


	if re.findall('💠 Batalkan', teks):
		pesan = 'waduh Kenapa Dibatalkan...?'
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=start'
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
		print(keamanannya())
		idd = message.from_user.id
		popoawwal = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		pageawal = requests.get(popoawwal)
		kokoawal = pageawal.json()['data']['status']
		if kokoawal == 'brand kosong':
			bot.send_message(message.chat.id,'Anda Belum Buat Brand Silahkan Buat Dulu', reply_markup=brandkosong1())
		else:
			idd = message.from_user.id
			popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=profil&id="+ str(idd)
			page = requests.get(popo)
			link = page.json()[0]['link']
			linktersedia = page.json()[0]['piket']
			paket = page.json()[0]['paket']
			tanggalberakhir = page.json()[0]['tanggalberakhir']
			nama = page.json()[0]['nama']
			popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=perbaikitanggal&id="+ str(tanggalberakhir)
			page1 = requests.get(popo1)
			alhir = ''
			if paket == 'easy':
				alhir = 'Aktif Selamanya'
			else:
				alhir = page1.json()['data']['ket']

			mama ='»» Profil ««\n\n🆔 ID Pengguna : '+str(idd)+'\n💎 Nama Brand : '+nama+'\n🧰 Paket : '+paket+'\n📬 Link Dibuat : '+str(link)+'\n📭 Total Link Tersedia : '+str(linktersedia)+'\n📆 Akhir Paket : '+alhir+'\nℹ️ bot coba klik link\n'
			bot.send_message(message.chat.id, mama)

	if re.findall('🗃 News',teks):
		bot.send_message(message.chat.id, 'masih Diperbaiki')

			
	if re.findall('💠 Harga Coin', teks):
		bot.send_message(message.chat.id, "Silahkan Pilih Coin", reply_markup=harga1())

	if re.findall('🌐 Smart Contract', teks):
		bot.send_message(message.chat.id, "Smart Contract\n0x09929382983287823872837283238")

	if re.findall('💠 Buat Link', teks):
		idd = message.from_user.id
		popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		page = requests.get(popo)
		koko = page.json()['data']['status']


		markup = types.ReplyKeyboardMarkup()
		b =  types.KeyboardButton("◀️️ Kembali")
		markup.resize_keyboard = True
		markup.one_time_keyboard = False
		markup.row(b)

		if koko == 'brand kosong':
			bot.send_message(message.chat.id,"Anda Belum Bisa Membuat Link Karena Anda Belum Membuat Brand\nSilahkan Membuat Brand Dulu.", reply_markup=brandkosong1())
		else:
			idd = message.from_user.id
			popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=cekpaket&id="+ str(idd)
			page1 = requests.get(popo1)
			status = page1.json()['data']['status']
			ket = page1.json()['data']['ket']
			if status == 'true':
				bot.send_message(message.chat.id,'Silahkan Tunggu...',reply_markup=markup)
				popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=LinkPendek'
				page1 = requests.get(popo1)
				bot.send_message(message.chat.id,"Silahkan Masukkan Link Pendek Anda\nhasilnya seperti contoh:\n\ncobaklik,link/brand-(linkpendek)\n\nCukup Masukkan untuk Kata Dalam Kurung")
			else:
				bot.send_message(message.chat.id,ket,reply_markup=awak())

	if re.findall('❇️ Link WA', teks):

		idd = message.from_user.id
		popoawwal = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		pageawal = requests.get(popoawwal)
		kokoawal = pageawal.json()['data']['status']
		if kokoawal == 'brand kosong':
			bot.send_message(message.chat.id,'Anda Belum Buat Brand Silahkan Buat Dulu', reply_markup=brandkosong1())
		else:
			idd = message.from_user.id
			popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=linkwa&id="+ str(idd)
			page = requests.get(popo)

			popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=ambilnomorwa&id="+ str(idd)
			page1 = requests.get(popo1)
			linkwa = page.json()[0]['pendek']
			nomorwa = page1.json()['data']['ket']
		
			markup = InlineKeyboardMarkup()
			markup.width = 2
			markup.add(
				InlineKeyboardButton("🌐 Launch", 'cobaklik.link/' + linkwa),
				InlineKeyboardButton("📦 Kirim Link", 'https://api.whatsapp.com/send/?phone=&text='+'hai...\nini link wa ku\ncobaklik.link/' + linkwa)
			)
		
			mama ='»» Link Whatsapp Kamu ««\n\n# Ini Nomor Whatsapp Kamu\n📞 '+nomorwa+'\n\n# ini Link Whatsapp Kamu\n⛓ cobaklik,link/'+linkwa
			bot.send_message(message.chat.id, mama,reply_markup=gantinomorwa())
			bot.send_message(message.chat.id,'🎁 Jika Link Diatas di Klik , Akan langsung menuju ke whatsapp kamu\n🎁 untuk test dan kirim linknya\nsilahkan klik tombol dibawah ini.', reply_markup=markup)


	if re.findall('🛄 Semua Link', teks):
		idd = message.from_user.id
		popoawwal = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=awal&id="+ str(idd)
		pageawal = requests.get(popoawwal)
		kokoawal = pageawal.json()['data']['status']
		if kokoawal == 'brand kosong':
			bot.send_message(message.chat.id,'Anda Belum Buat Brand Silahkan Buat Dulu', reply_markup=brandkosong1())
		else:
			idd = message.from_user.id

			popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=profil&id="+ str(idd)
			page1 = requests.get(popo1)

			totalklik = page1.json()[0]['semuaklik']
			totallink = page1.json()[0]['link']

			popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=statistik&id="+ str(idd)
			page = requests.get(popo)
			mama ='🗄Total Link Yang Kamu Buat : '+str(totallink)+'\n📐 Total Semua Klik : '+str(totalklik)
			#bot.send_message(message.chat.id, '»» Semua Link ««\n\n')
			aa = page.json()
			asa = 0
			pertama = aa[0]['id']
			semualink = ''
						
			for c in aa: 
				asa = asa + 1
				idaaaaa = c['id']
				if idaaaaa == pertama:
					semualink += 'cobaklik.link/' + c['link']+'\n'
					markup = InlineKeyboardMarkup()
					markup.width = 1
					markup.add(
						InlineKeyboardButton('cobaklik.link/' + c['link'], 'cobaklik.link/' + c['link'])
					)
					markup.add(
						InlineKeyboardButton(str(c['klik'])+" Klik", 'cobaklik.link/' + c['link']),
						InlineKeyboardButton("⭕️ Hapus", callback_data='Tidakbisahapus'),
						InlineKeyboardButton("📦 Kirim Link", 'https://api.whatsapp.com/send/?phone=&text='+'hai\nini link ku\ncobaklik.link/' + c['link']),
						InlineKeyboardButton("🌐 Klik", 'cobaklik.link/' + c['link'])
					)
					bot.send_message(message.chat.id, str(asa), reply_markup=markup)
				else:
					semualink += 'cobaklik.link/' + c['link']+'\n'
					markup = InlineKeyboardMarkup()
					markup.width = 1
					markup.add(
						InlineKeyboardButton('cobaklik.link/' + c['link'], 'cobaklik.link/' + c['link'])
						
					)
					markup.add(
						InlineKeyboardButton(str(c['klik'])+" Klik", 'cobaklik.link/' + c['link']),
						InlineKeyboardButton("⭕️ Hapus", 'cobaklik.link/hapus.php?id=' + c['id']),
						InlineKeyboardButton("📦 Kirim Link", 'https://api.whatsapp.com/send/?phone=&text='+'hai\nini link ku\ncobaklik.link/' + c['link']),
						InlineKeyboardButton("🌐 Klik", 'cobaklik.link/' + c['link'])
						
					)
					bot.send_message(message.chat.id, str(asa), reply_markup=markup)

			markup = InlineKeyboardMarkup()
			markup.width = 1
			markup.add(
				InlineKeyboardButton("📤 Kirim Semua Link", 'https://api.whatsapp.com/send/?phone=&text='+semualink)
			)
			bot.send_message(message.chat.id, mama, reply_markup=markup)

	if re.findall('♻️ Bantuan', teks):
		bot.send_message(message.chat.id,"Silahkan Pilih Salah Satu Kontak Dibawah ini", reply_markup=bantuan())
	if re.findall('🆎 About', teks):
		idd = message.from_user.id
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=about'
		page1 = requests.get(popo1)

		markup = types.ReplyKeyboardMarkup()
		a =  types.KeyboardButton("💠 Harga Coin")
		b =  types.KeyboardButton("◀️️ Kembali")
		markup.resize_keyboard = True
		markup.one_time_keyboard = False
		markup.row(b,a)
		bot.send_message(message.chat.id, "Silahkan Cek Harga Coin Dengan Menekan Tombol di Bawah",reply_markup=markup)

	if re.findall('🛅 Buat Brand', teks):
		pesan = 'Membuat Brand\n\nbrand berfungsi menjadi id link anda\nmisal brand anda bernama "koko"\nmaka, link yang didapatkan adalah\n1. Untuk Menuju ke chat whatsapp akan mendaparkan "cobaklik*link/koko"\n2. Untuk Link produk akan mendapatkan "cobaklik*link/koko-linkanda" dan linkanda bisa di custom sesuai keinginans'
		bot.send_message(message.chat.id, pesan,reply_markup=tombolbuatbrand())
	
	if re.findall('💠 Ganti Nomor Whatsapp', teks):
		pancerbatal = '💠 Ganti Nomor Whatsapp'
		idd = message.from_user.id
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=GantiWa'
		page1 = requests.get(popo1)

		markup = types.ReplyKeyboardMarkup()
		b =  types.KeyboardButton("💠 Batalkan")
		markup.resize_keyboard = True
		markup.one_time_keyboard = False
		markup.row(b)

		bot.send_message(message.chat.id, "Silahkan Masukkan Nomor Whatsapp Anda",reply_markup=markup)
	
	if re.findall('📬 Paket', teks):
		bot.send_message(message.chat.id, "Masih Diperbaiki")

	if re.findall('💠 Masukkan Brand Anda', teks):
		pancerbatal = '💠 Masukkan Brand Anda'
		idd = message.from_user.id
		popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=buatbrand'
		page1 = requests.get(popo1)
		markup = types.ReplyKeyboardMarkup()
		b =  types.KeyboardButton("💠 Batalkan")
		markup.resize_keyboard = True
		markup.one_time_keyboard = False
		markup.row(b)
		bot.send_message(message.chat.id,"Silahkan Masukkan Nama Brand Anda",reply_markup=markup)

	else:
		if re.findall('💠', teks):
			pass
		else:
			idd = message.from_user.id
			popo = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=ambillogbot&id="+ str(idd)
			page = requests.get(popo)
			status = page.json()['data']['status']

			if status == 'buatbrand':
				bot.send_message(message.chat.id, 'Nama Brand Yang Kamu Pilih : '+teks+'\nSilahkan Tunggu....')
				idd = message.from_user.id
				popo1 = 'https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=buatbrand&id='+str(idd)+'&brand='+teks;
				page1 = requests.get(popo1)
				koko1 = page1.json()[0]['status']
				ket = page1.json()[0]['ket']
				if ket == 'ook':
					idd = message.from_user.id
					popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=start'
					page1 = requests.get(popo1)
					bot.send_message(message.chat.id,'Anda Sukses Membuat Brand',reply_markup=awak())
				else:
					bot.send_message(message.chat.id,ket+'\nSilahkan Masukkan Brand Anda Lagi, Atau Klik Kembali',reply_markup=tombolbuatbrand())

			if status == 'LinkPendek':
				bot.send_message(message.chat.id, 'Link Pendek Yang Kamu Masukkan : '+teks+'\nSilahkan Tunggu....')
				idd = message.from_user.id
				popo1 = 'https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=buatlink1&id='+str(idd)+'&linkpendek='+teks;
				page1 = requests.get(popo1)
				status = page1.json()['data']['status']
				ket = page1.json()['data']['ket']

				if status == 'true':
					markup = types.ReplyKeyboardMarkup()
					b =  types.KeyboardButton("◀️️ Kembali")
					markup.resize_keyboard = True
					markup.one_time_keyboard = False
					markup.row(b)
					idd = message.from_user.id
					popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=LinkTujuan'
					page1 = requests.get(popo1)
					bot.send_message(message.chat.id,"Silahkan Copy Link Tujuan Anda, Dan Masukkan Kesini Sebagai Link Tujuan",reply_markup=markup)
				else:
					bot.send_message(message.chat.id,ket)
			if status == 'LinkTujuan':
				bot.send_message(message.chat.id, 'Link Tujuan Yang Kamu Masukkan : \n'+teks+'\nSilahkan Tunggu....')
				idd = message.from_user.id
				popo1 = 'https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=buatlink2&id='+str(idd)+'&linktujuan='+teks;
				page1 = requests.get(popo1)
				status = page1.json()['data']['status']
				ket = page1.json()['data']['ket']

				if status == 'true':
					idd = message.from_user.id
					popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=start'
					page1 = requests.get(popo1)
					bot.send_message(message.chat.id,ket,reply_markup=awak())
				else:
					bot.send_message(message.chat.id,ket)

			if status == 'GantiWa':
				idd = message.from_user.id
				popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=gantiwanya&id="+str(idd)+'&nomorwa='+str(teks)
				page1 = requests.get(popo1)
				status = page1.json()['data']['status']
				ket = page1.json()['data']['ket']

				if status == 'true':
					idd = message.from_user.id
					popo1 = "https://cobaklik.link/botuser.php?keamanan="+str(keamanan)+"&pancer=logbot&id="+ str(idd)+'&log=start'
					page1 = requests.get(popo1)
					bot.send_message(message.chat.id,'>>Sukses<<\n\nAnda Sukses Mengganti Nomor Whatsapp',reply_markup=awak())
				else:
					bot.send_message(message.chat.id,'>>Gagal<<\n\n'+ket)













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
	if call.data == "Tidakbisahapus":
		bot.delete_message(call.message.chat.id, call.message.message_id)
		pesan = 'Link Standar Tidak Bisa Dihapus'
		bot.send_message(call.message.chat.id, pesan)
	else:
		if re.findall('cobaklik.link/hapus.php', call.data):
			bot.delete_message(call.message.chat.id, call.message.message_id)
			pesan = 'buka link untuk menghapus'
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
	a =  types.KeyboardButton("💠 Ganti Nomor Whatsapp")
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
	e =  types.KeyboardButton("💠 Buat Link")
	g =  types.KeyboardButton("♻️ Bantuan")
	h =  types.KeyboardButton("🆎 About")
	i =  types.KeyboardButton("📬 Paket")
	j =  types.KeyboardButton("🗃 News")
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
	e =  types.KeyboardButton("💠 Buat Link")
	g =  types.KeyboardButton("♻️ Bantuan")
	h =  types.KeyboardButton("🆎 About")
	i =  types.KeyboardButton("📬 Paket")
	j =  types.KeyboardButton("🗃 News")
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
# ketik command pip freeze > requirements.txt

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
