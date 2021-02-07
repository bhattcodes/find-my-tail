import eel
import Find_My_Tail

eel.init('web')

@eel.expose
def locations():
	return Find_My_Tail.stores_string()

eel.start()

eel.start('index.html')