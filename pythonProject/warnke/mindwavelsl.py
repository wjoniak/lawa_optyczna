import mindwavelsl

mwlsl = MindwaveLSL('localhost', 13854)

# Setup the LSL outlet and the ThinkGear connection
mwlsl.setup()

# Run the service
mwlsl.run()