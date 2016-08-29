import fetchurls
import sys
from urllib.parse import urlparse

if len(sys.argv) != 2:
	sys.exit(0)
print('fetching_base_url')
url=urlparse(sys.argv[1])

"""if url.netloc == "":
	base=url.path
else:
	base=url.netloc"""

base=a=url.scheme+"://"+url.netloc
i=fetchurls.fetching(base,sys.argv[1])

j=[]
for a in i:
	j=j+fetchurls.fetching(base,a)


print('fetching_done')
j=i+j
j=set(j)
j=list(j)

#p=[]
#for a in j:
#	p=p+fetchurls.fetching(a)

#p=i+j+p
#p=set(p)
#p=list(p)	
f=open('crawlerdata.txt','a')
for k in j:
	f.write(str(k)+'\n')
f.close()
#j=j+i
#j=set(j)
#j=list(j)
