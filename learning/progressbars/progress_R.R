
tot = 50
for (i in 1:50){
	Sys.sleep(1)
	cat(
		paste0(paste0(rep('*', i), collapse=''), 
		paste0(rep('=', tot-i), collapse='')),
		"| ",
		as.character(i*2),
		'%',
		end='\r')
}