@echo off
set bin_path=%cd%
cd ../

@echo on
python -m blackjack_python

@echo off
cd %bin_path%
