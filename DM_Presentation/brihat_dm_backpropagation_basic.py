import math

def main():
    print("Classification by Backpropagation")
    print("Brihat Ratna Bajracharya\n19/075\n\n")

    i1 = 0.05
    i2 = 0.1

    o1 = 0.01
    o2 = 0.99

    w1 = 0.15
    w2 = 0.20
    w3 = 0.25
    w4 = 0.30

    w5 = 0.40
    w6 = 0.45
    w7 = 0.50
    w8 = 0.55

    b1 = 0.35
    b2 = 0.60

    alpha = 0.5

    eo1 = 100
    eo2 = 100

    run_again = True
    iteration = 0
    while(run_again):
        h1 = 1.0 / (1.0 + math.exp(-1.0 * (w1 * i1 + w2 * i2 + b1)))
        # print("h1:", h1)
        iteration = iteration + 1
        # print(iteration)

        h2 = 1.0 / (1.0 + math.exp(-1.0 * (w3 * i1 + w4 * i2 + b1)))
        # print("h2:", h2)


        y1 = 1.0 / (1.0 + math.exp(-1.0 * (w5 * h1 + w6 * h2 + b2)))
        # print("y1:", y1)


        y2 = 1.0 / (1.0 + math.exp(-1.0 * (w7 * h1 + w8 * h2 + b2)))
        # print("y2:", y2)

        eo1 = 0.5 * math.pow((o1 - y1),2)
        # print("eo1:", eo1)

        eo2 = 0.5 * math.pow((o2 - y2),2)
        # print("eo2:", eo2)

        etotal = eo1 + eo2
        # print("etotal:", etotal)

        # for ew5
        def_etotal_y1 = - 1.0 * (o1 - y1)
        # print(def_etotal_y1)

        def_y1_o1 = y1 * (1.0 - y1)
        # print(def_y1_o1)

        def_y1_w5 = h1
        # print(def_y1_w5)

        def_etotal_w5 = def_etotal_y1 * def_y1_o1 * def_y1_w5
        # print(def_etotal_w5)

        w5new = w5 - alpha * def_etotal_w5
        # print("w5new:", w5new)


        # for ew6
        # def_etotal_y1 = - 1.0 * (o1 - y1)
        # print(def_etotal_y1)

        # def_y1_o1 = y1 * (1.0 - y1)
        # print(def_y1_o1)

        def_y1_w6 = h2
        # print(def_y1_w6)

        def_etotal_w6 = def_etotal_y1 * def_y1_o1 * def_y1_w6
        # print(def_etotal_w6)

        w6new = w6 - alpha * def_etotal_w6
        # print("w6new:", w6new)


        # for ew7
        def_etotal_y2 = - 1.0 * (o2 - y2)
        # print(def_etotal_y2)

        def_y2_o2 = y2 * (1.0 - y2)
        # print(def_y2_o2)

        def_y2_w7 = h1
        # print(def_y2_w7)

        def_etotal_w7 = def_etotal_y2 * def_y2_o2 * def_y2_w7
        # print(def_etotal_w7)

        w7new = w7 - alpha * def_etotal_w7
        # print("w7new:", w7new)


        # for ew8
        # def_etotal_y2 = - 1.0 * (o2 - y2)
        # print(def_etotal_y2)

        # def_y2_o2 = y2 * (1.0 - y2)
        # print(def_y2_o2)

        def_y2_w8 = h2
        # print(def_y2_o2)

        def_etotal_w8 = def_etotal_y2 * def_y2_o2 * def_y2_w8
        # print(def_etotal_w8)

        w8new = w8 - alpha * def_etotal_w8
        # print("w8new:", w8new)


        '''for w1, w2, w3, w4'''
        # for w1
        def_e1_y1 = def_etotal_y1 * def_y1_o1
        # print(def_e1_y1)

        def_y1_h1 = w5
        # print(def_y1_h1)

        def_e1_h1 = def_e1_y1 * def_y1_h1
        # print(def_e1_h1)
        #-------

        def_e2_y2 = def_etotal_y2 * def_y2_o2
        # print(def_e2_y2)

        def_y2_h1 = w7
        # print(def_y2_h1)

        def_e2_h1 = def_e2_y2 * def_y2_h1
        # print(def_e2_h1)

        def_etotal_h1 = def_e1_h1 + def_e2_h1
        # print(def_etotal_h1)
        #--------

        def_h1 = h1 * (1.0 - h1)
        # print(def_h1)

        def_h1_w1 = i1
        # print(def_h1_w1)

        #-------
        def_etotal_w1 = def_etotal_h1 * def_h1 * def_h1_w1
        # print(def_etotal_w1)

        w1new = w1 - alpha * def_etotal_w1
        # print("w1new:", w1new)

        ###########################

        # for w2
        '''def_etotal_h1 from above'''
        #--------

        def_h1 = h1 * (1.0 - h1)
        # print(def_h1)

        def_h1_w2 = i2
        # print(def_h1_w2)

        #-------
        def_etotal_w2 = def_etotal_h1 * def_h1 * def_h1_w2
        # print(def_etotal_w2)

        w2new = w2 - alpha * def_etotal_w2
        # print("w2new:", w2new)

        ''' not now '''
        ###########################

        # for w3
        def_e1_y1 = def_etotal_y1 * def_y1_o1
        # print(def_e1_y1)

        def_y1_h2 = w6
        # print(def_y1_h2)

        def_e1_h2 = def_e1_y1 * def_y1_h2
        # print(def_e1_h2)
        #-------

        def_e2_y2 = def_etotal_y2 * def_y2_o2
        # print(def_e2_y2)

        def_y2_h2 = w8
        # print(def_y2_h2)

        def_e2_h2 = def_e2_y2 * def_y2_h2
        # print(def_e2_h2)

        def_etotal_h2 = def_e1_h2 + def_e2_h2
        # print(def_etotal_h2)
        #-----------

        def_h2 = h2 * (1.0 - h2)
        # print(def_h2)

        def_h2_w3 = i1
        # print(def_h2_w3)

        #-------
        def_etotal_w3 = def_etotal_h2 * def_h2 * def_h2_w3
        # print(def_etotal_w3)

        w3new = w3 - alpha * def_etotal_w3
        # print("w3new:", w3new)

        ''' not now '''
        ###########################

        # for w4
        '''def_etotal_h2 from above'''
        #-----------

        def_h2 = h2 * (1.0 - h2)
        # print(def_h2)

        def_h2_w4 = i2
        # print(def_h2_w4)

        #-------
        def_etotal_w4 = def_etotal_h2 * def_h2 * def_h2_w4
        # print(def_etotal_w4)

        w4new = w4 - alpha * def_etotal_w4
        # print("w4new:", w4new)

        w5 = w5new
        w6 = w6new
        w7 = w7new
        w8 = w8new

        w1 = w1new
        w2 = w2new
        w3 = w3new
        w4 = w4new

        # run_again = eo1 > 0.00000001 or eo2 > 0.00000001
        run_again = iteration < 10000
        # run_again = False


    print("After " + str(iteration) + " iterations...\n")
    print("w1: ", w1)
    print("w2: ", w2)
    print("w3: ", w3)
    print("w4: ", w4)
    print("w5: ", w5)
    print("w6: ", w6)
    print("w7: ", w7)
    print("w8: ", w8)

    h1 = 1.0 / (1.0 + math.exp(-1.0 * (w1 * i1 + w2 * i2 + b1)))
    h2 = 1.0 / (1.0 + math.exp(-1.0 * (w3 * i1 + w4 * i2 + b1)))


    y1 = 1.0 / (1.0 + math.exp(-1.0 * (w5 * h1 + w6 * h2 + b2)))
    y2 = 1.0 / (1.0 + math.exp(-1.0 * (w7 * h1 + w8 * h2 + b2)))

    print("y1: ", y1)
    print("y2: ", y2)


if __name__ == "__main__":
    main()
