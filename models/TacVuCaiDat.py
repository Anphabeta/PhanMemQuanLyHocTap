import repositories.RepoCaiDat as RepoCaiDat
from lang.strings import set_language

def layThongTinCaiDat():
	return RepoCaiDat.layThongTinCaiDat()

def suaThongTinCaiDat(data):
	RepoCaiDat.suaThongTinCaiDat(data)

	data = RepoCaiDat.layThongTinCaiDat()
	set_language(data['lang'])


