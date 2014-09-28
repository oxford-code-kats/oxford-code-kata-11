
def main(methods=None):
    import sorter
    import time
    timings = []
    if methods is None:
        # methods = ['insert_naive', 'insert_slow']
        methods = [name for name in dir(sorter)
                    if name.startswith("insert_")]
    import random
    items = range(1,1000)
    random.shuffle(items)
    for method_name in methods:
        print "Testing", method_name
        insert_method = getattr(sorter, method_name)
        test_sorter = sorter.Sorter1(insert_method)
        start_time = time.time()
        for i in items:
            test_sorter.add(i)
            test_sorter.as_list()
        timings.append((time.time()-start_time, method_name))
    print "Done Testing"
    print timings

main()

