def p95(values): return sorted(values)[max(0,int(len(values)*0.95)-1)]
if __name__=="__main__": print(p95([38,42,41]))
