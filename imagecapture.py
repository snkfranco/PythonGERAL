import cv2 

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check) 
        cv2.imshow("Capturando", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='salva_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('salva_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Imagem Capturada", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()

            img_ = cv2.imread('salva_img.jpg', cv2.IMREAD_ANYCOLOR)
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            img_ = cv2.resize(gray,(500,400))
            img_resized = cv2.imwrite(filename='salva_img-final.jpg', img=img_)
        
            break
        elif key == ord('q'):
            print("Desligando Câmera")
            webcam.release()
            print("Câmera off")
            print("Programa encerrado")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Desligando Câmera")
        webcam.release()
        print("Câmera off")
        print("Programa encerrado")
        cv2.destroyAllWindows()
        break
