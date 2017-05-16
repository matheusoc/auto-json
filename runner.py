import json
import sys
reload(sys)
sys.setdefaultencoding('latin-1')

if __name__ == '__main__':
	file = open('patterns/simple-message.json', 'r+')

	file_json =  json.load(file)

	file.close()

	print json.dumps(file_json, sort_keys=True)

	name = raw_input('File name: ')
	text = raw_input('Data to send: ')

	new_json_file = open('contents/'+name, 'w+')

	file_json['message']['text'] = str(text)

	new_json_file.write(json.dumps(file_json, indent=4))

	new_json_file.close()

	data = json.dumps(file_json, ensure_ascii=False, encoding='utf-8')

	print data.encode('latin-1').decode('utf-8')
