import PyPDF2


f = open('data.pdf', 'rb')

pdf = PyPDF2.PdfFileReader(f)
pgs = pdf.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

for pg in range(pgs):

    p = pdf.getPage(pg)
    o = p.getObject()


    ann = o[key]
    for a in ann:
        u = a.getObject()
        #if u[ank].has_key(uri):
        print(u[ank][uri])
