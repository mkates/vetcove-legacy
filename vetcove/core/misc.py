### Miscellaneous helper functions ###

def convertIntegerDollarsToFloatDollars(value):
	
	''' Takes a dollar amount in integer format, and formats it
	to a readable dollar amount. For example, 123456 would be
	converted to $1,234.56. If there is no amount provided, it
	returns $0.00'''

	if not value:
		value = '0'
	value = str(int(value))
	value = value.zfill(3)
	dollars = list(value[0:-2])
	for i in range(len(value)-5,0,-3):
		dollars.insert(i,',')
	dollars = "".join(dollars)
	if not dollars:
		dollars = '0'
	return "$"+dollars+'.'+value[-2:]