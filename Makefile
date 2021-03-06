run:
	python main.py

test:
	rm -rf test_dir_copy
	cp -r test_dir test_dir_copy
	cd test_dir_copy; python ../main.py
	cd test_dir_copy; tar -xf dir_1.tar.xz
	cd test_dir_copy; tar -xf dir_2.tar.xz
	cd test_dir_copy; tar -xf test_dir_copy.tar.xz
	cd test_dir_copy; rm *.tar.xz
