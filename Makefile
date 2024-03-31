.PHONY: test-park
test-park:
	pytest Selenium/code/test_login.py --url='https://park.vk.company/'
