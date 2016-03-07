all:
	sh get_phone_log.sh
	python3 _2_push_diffreneces_to_shell_.py Az storage/9016-4EF8/Music
	sh push.sh