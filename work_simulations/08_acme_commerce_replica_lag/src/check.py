def is_stale(source_version,read_version): return read_version<source_version
if __name__=="__main__": print(is_stale(10,9))
