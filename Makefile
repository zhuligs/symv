# python bin
PYBIN = /usr/bin/python

default:
	export PYTHONPATH=`pwd`/lib/python
	$(PYBIN) setup.py install --home=.
	@if [ -d lib64 ]; then echo export PYTHONPATH=`pwd`/lib64/python':$$PYTHONPATH' > symvvars.sh; \
	   	else echo export PYTHONPATH=`pwd`/lib/python':$$PYTHONPATH' > symvvars.sh;fi
	@echo export PATH=`pwd`':$$PATH' >> symvvars.sh
	@echo
	@echo please add \" source `pwd`/symvvars.sh \" in $$HOME/.bashrc
	@echo
	

.PHONY : clean

clean:
	-rm -rf build lib lib64 caly.sh

