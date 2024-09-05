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
	@/bin/bash ./cicd/release_prepare

release-start:
	@/bin/bash ./cicd/release_start

release-pypi:
	@/bin/bash ./cicd/release_pypi

release-android:
	@/bin/bash ./cicd/release_android
