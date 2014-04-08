pygame.camera.init()

coint = 1

def camtest():
	global coint
	img = cam.get_image()
	pygame.image.save(img, (str(coint) + ".bmp"))
	pygame.camera.quit()
	coint +=1
	print "done!"

camtest()
camtest()