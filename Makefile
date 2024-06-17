clean:
	rm -rf venv

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

main-net-restart:
	LC_ALL=en_US.utf-8 ansible-playbook ansible/bitdust_refresh.yml -i ansible/inventory/main -e "application_name=main"

main-net-config-update:
	LC_ALL=en_US.utf-8 ansible-playbook ansible/telegraf.yml -i ansible/inventory/main -K -e "application_name=main"

release-prepare:
	@cd ./cicd && /bin/bash release_prepare

release-start:
	@cd ./cicd && /bin/bash release_start

release-pypi:
	@cd ./cicd && /bin/bash release_pypi

release-android:
	@cd ./cicd && /bin/bash release_android
