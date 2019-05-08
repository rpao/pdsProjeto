from echo import Echo

input_file = 'arquivos\sp04.wav'
output_file = 'arquivos\sp04echo.wav'

offset = 500
factor = 0.5

echo = Echo()
echo.generate_audioEcho(input_file,output_file,offset, factor)
echo.play_input()
echo.play_output()
