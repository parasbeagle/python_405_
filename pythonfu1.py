#!/usr/bin/python
##from pdb import gimp_equalize
##from pdb import gimp_image_rotate
##from pdb import file_jpeg_load, file_jpeg_save
##from pdb import gimp_image_get_active_drawable
class m:
    def __init__(self):
        self.rotequ()
    def Files(self,ext,rLim=15):
        q=[]
        for a in range(1,rLim+1):
            fname = '%04d.' % (a)
            q.append(fname+ext)
        return q
    def rotequ(self):
        for f,q in zip(Files('jpeg'), Files('jpg')):
            quality = 1
            smoo=0.5; optm=0; prog=0; comment=''
            subsmp=0,
            baseline=1;
            res=0; dct=0
            image = pdb.file_jpeg_load(f,f)
            pdb.gimp_image_rotate(image,2)
            drawable = pdb.gimp_image_get_active_drawable(image)
            pdb.gimp_equalize(drawable, 0)
            pdb.file_jpeg_save(image,drawable,q,q,quality,smoo,optm,comment,subsmp,baseline,res,dct)
