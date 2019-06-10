import numpy as np
import cv2

video = cv2.VideoCapture('arquivos/video1.avi')

## informacoes do video
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH ))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT ))
fps =  int(video.get(cv2.CAP_PROP_FPS))

## arquivos que armazenam o resultado
videoFinal = cv2.VideoWriter('arquivos/relatorio/video1_resultado.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, (width,height))
videoFinalBlur = cv2.VideoWriter('arquivos/relatorio/video1_resultado_blur.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, (width,height))

## quando ret = False, chegou ao fim do video
## primeiro frame do video
ret, frameI = video.read()

## aplica reducao de ruidos 'gaussian blur'
frameIBlur = cv2.GaussianBlur(frameI, (5, 5), 0)
cont = 0
while(True):
    ret, frame = video.read()
    if (ret == False): break

    ## calcula a diferenca absoluta entre o primeiro frame e o frame atual
    frameDif = cv2.absdiff(frameI, frame)
    _, frameDif = cv2.threshold(frameDif, 25, 255, cv2.THRESH_BINARY)
    frameDif = (255 - frameDif) ## inverter cores
    videoFinal.write(frameDif)

    ## aplica reducao de ruidos 'gaussian blur'
    frameBlur = cv2.GaussianBlur(frame, (5, 5), 0)
    
    ## calcula a diferenca absoluta entre o primeiro frame e o frame atual com blur
    frameDifBlur = cv2.absdiff(frameIBlur, frameBlur)
    _, frameDifBlur = cv2.threshold(frameDifBlur, 25, 255, cv2.THRESH_BINARY)
    frameDifBlur = (255 - frameDifBlur) ## inverter cores
    videoFinalBlur.write(frameDifBlur)

    frameI = frame
    frameIBlur = frameBlur

    ## salva um frame por segundo
    if (cont%10) == 0:
        cv2.imwrite('arquivos/relatorio/%d_originl.jpg'%cont, frame)
        cv2.imwrite('arquivos/relatorio/%d_semBlur.jpg'%cont, frameDif)
        cv2.imwrite('arquivos/relatorio/%d_comlur.jpg'%cont, frameDifBlur)
    
    cont += 1

video.release()
videoFinal.release()
videoFinalBlur.release()
cv2.destroyAllWindows()
