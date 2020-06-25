import altiwx
import subprocess

frame_file = altiwx.filename + ".txt"
command = "demodPOES -s 48 '" + altiwx.input_file + "' -o '" + frame_file + "'"
subprocess.Popen([command], shell=1).wait()

output_file = filename + "/msa.png"
command = "java -jar NOAA_HIRS_Decoder.jar config.ini '" + frame_file + "'"
subprocess.Popen([command], shell=1).wait()
