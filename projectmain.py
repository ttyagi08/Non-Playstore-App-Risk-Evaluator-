from literadar import LiteRadar
apk_path = '/home/tanmay/Downloads/Flashlight_LED_Torch_v1.7.4.apk'
lrd = LiteRadar(apk_path)
res = lrd.compare()
print(json.dumps(res, indent=4, sort_keys=True))