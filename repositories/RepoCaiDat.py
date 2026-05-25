import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTING_PATH = os.path.join(BASE_DIR,"data","settings.json")

def layThongTinCaiDat():
	try:
		with open(SETTING_PATH, "r") as settingFile:
			data = json.load(settingFile)

		return data

	except json.JSONDecoderError:
		print("Json sai cú pháp")

		return {}


def suaThongTinCaiDat(data):
	with open(SETTING_PATH, 'w') as settingFile:
		json.dump(data,settingFile)




