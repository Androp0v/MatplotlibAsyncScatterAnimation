# MatplotlibAsyncScatterAnimation

Simple demonstration on how to use matplotlib's animation module to read and plot scatter data being generated or read in an asynchronous process (using Python's multiprocessing library).

*numGen* is the function that generates the data in a separate process and puts it in a queue for the main GUI with matplotlib to read and plot it. The data generated is a gaussian distribution in both x and y coordinates, centered in (0,0).

Hence, the GUI is fully responsive and the window can be resized on the fly, since data is being generated in a different process (so the main thread is never blocked). Blit is used to allow the figure to be updated without redrawing the whole figure every time.
