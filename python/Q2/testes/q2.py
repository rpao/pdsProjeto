from echo import Echo

echo = Echo()
echo.open('arquivos/sp04.wav')
echo.input_wave()
echo.delay()
echo.output_wave('arquivos/sp04_output_class.wav')
echo.play_input()
echo.play_output()
