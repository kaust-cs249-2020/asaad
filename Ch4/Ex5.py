#  4.7 Mass Spectrometry Meets Golf 
from Ex3 import CyclicSpectrum, constructAminoAcidMass, LinearSpectrum

aminoAcidMass = constructAminoAcidMass()

# def score(peptide, spectrum):
#     theorticalspectrum = CyclicSpectrum(peptide, aminoAcidMass)
#     if type(spectrum) != list:
#         expSpectrum = [int(x) for x in spectrum.split(" ")]
#     else:
#         expSpectrum = [int(x) for x in spectrum]

#     score = 0
#     for mass in theorticalspectrum:
#         if mass in expSpectrum:
#             theorticalspectrum.remove(mass)
#             score = score + 1
#     return score

def score(peptide, spectrum):
    """
    given a peptide and a spectrum,
    return the count of the number of matches between cyclic spectrum of peptide and spectrum
    """
    if type(spectrum) != list:
        expSpectrum = [int(x) for x in spectrum.split(" ")]
    else:
        expSpectrum = [int(x) for x in spectrum]
    count = 0
    for x in CyclicSpectrum(peptide, aminoAcidMass):
        if x in expSpectrum:
            count += 1
            expSpectrum.remove(x)
    return count
    
def linearscore(peptide, spectrum):
    theorticalspectrum = LinearSpectrum(peptide, aminoAcidMass)
    if type(spectrum) != list:
        expSpectrum = [int(x) for x in spectrum.split(" ")]
    else:
        expSpectrum = [int(x) for x in spectrum]
    score = 0
    for mass in expSpectrum:
        if mass in theorticalspectrum:
            theorticalspectrum.remove(mass)
            score = score + 1
    return score

def trim(leaderBoard, Spectrum, N):
    peptides = {}
    trim_list = []
    for pep in leaderBoard:
        peptides[pep] = linearscore(pep, Spectrum)
    sortedPeptides = sorted(peptides.items(), key=lambda item: item[1], reverse=True)
    maximumValue = 0
    for i, pair in enumerate(sortedPeptides):
        if i < N:
            trim_list.append(pair[0])
            maximumValue = peptides[pair[0]]
        elif i>=N and pair[1] == maximumValue:
            trim_list.append(pair[0])
    return trim_list    

def expand(peptides):
    newPeptides = []
    for pep in peptides:
        for amino in aminoAcidMass.keys():
            newPeptides.append(pep + amino)
    return newPeptides


def mass(peptide):
    total = 0
    for pep in peptide:
        total += int(aminoAcidMass[pep])
    return total

def peptideToMass(peptide):
    mass = []
    for pep in peptide:
        mass.append(aminoAcidMass[pep])
    return mass

    
def LeaderboardCyclopeptideSequencing(Spectrum, N):
    leaderBoard = [""]
    Spectrum = [int(x) for x in Spectrum.split(" ")]
    leaderPeptide = ""
    while len(leaderBoard) > 0:
        leaderBoard = expand(leaderBoard)
        # print(candidatePeps)
        for pep in leaderBoard[:]:
            # print(pep, mass(pep))
            if mass(pep) == max(Spectrum):
                if linearscore(pep, Spectrum) > linearscore(leaderPeptide, Spectrum):
                    leaderPeptide = pep
            elif mass(pep) > max(Spectrum):
                leaderBoard.remove(pep)
        leaderBoard = trim(leaderBoard, Spectrum, N)
                # print("removed", pep)
        # print(finalPeps)
        # blacklist.append(pep)
        # print(candidatePeps)
    return peptideToMass(leaderPeptide)


if __name__ == "__main__":
    # print(" ".join(CyclopeptideSequencing("0 103 128 128 129 129 131 131 137 163 234 240 258 259 259 260 266 291 291 362 369 371 388 389 395 419 422 422 498 499 500 517 525 526 550 550 551 628 629 629 653 654 662 679 680 681 757 757 760 784 790 791 808 810 817 888 888 913 919 920 920 921 939 945 1016 1042 1048 1048 1050 1050 1051 1051 1076 1179")))
    # print(score("LRMQWRDEYYVFMHGGDHTKAVKWRNPCQFCKAIYDC", "0 57 57 71 71 71 87 99 101 103 113 113 113 114 114 115 115 115 128 128 128 128 128 129 131 131 131 131 137 137 147 147 147 147 156 156 163 163 163 170 172 184 184 194 199 199 215 216 218 218 227 229 229 234 238 244 251 252 259 259 259 262 268 269 270 275 275 276 276 277 278 278 286 287 287 292 294 294 298 298 300 309 312 325 331 331 347 347 349 353 358 362 362 366 366 366 372 381 382 391 391 399 399 400 401 405 406 406 407 408 409 410 415 415 415 422 422 426 429 433 433 437 462 462 467 472 475 476 481 486 487 490 493 494 494 494 497 503 503 514 520 527 528 529 529 536 536 537 538 538 543 546 552 553 554 557 561 562 562 564 564 565 569 585 590 591 595 599 600 604 607 609 618 621 623 625 628 631 634 644 650 651 656 656 658 664 666 666 667 668 674 675 677 678 683 692 692 692 693 695 699 701 708 709 709 713 713 715 732 735 738 738 746 754 762 763 765 770 778 779 780 781 781 784 791 795 797 803 805 806 814 814 819 822 823 823 824 824 827 828 829 834 836 837 839 852 855 862 863 869 876 882 885 885 891 893 893 893 894 898 902 909 910 922 925 926 927 928 934 937 942 948 951 951 952 953 953 960 962 965 965 967 968 968 969 970 990 991 993 1005 1006 1010 1013 1016 1022 1024 1030 1032 1033 1040 1040 1040 1049 1050 1054 1055 1056 1057 1063 1065 1066 1066 1066 1073 1081 1081 1082 1083 1091 1093 1093 1098 1116 1120 1120 1121 1121 1123 1125 1128 1131 1144 1152 1153 1155 1160 1161 1161 1163 1168 1169 1169 1180 1180 1180 1180 1185 1185 1186 1194 1196 1197 1203 1210 1221 1222 1228 1229 1229 1229 1235 1237 1238 1240 1245 1246 1249 1251 1256 1257 1265 1267 1268 1284 1284 1291 1291 1292 1294 1299 1300 1300 1308 1308 1313 1316 1317 1318 1324 1327 1332 1342 1343 1349 1350 1355 1357 1357 1358 1359 1360 1364 1368 1369 1372 1379 1382 1384 1387 1396 1400 1401 1412 1413 1414 1422 1428 1428 1431 1431 1439 1445 1447 1447 1447 1448 1455 1455 1455 1455 1457 1462 1463 1473 1474 1483 1483 1483 1485 1486 1487 1492 1497 1497 1502 1510 1515 1516 1516 1519 1527 1529 1531 1532 1542 1554 1557 1559 1560 1560 1560 1562 1576 1578 1583 1584 1586 1588 1594 1595 1596 1601 1602 1602 1602 1610 1611 1616 1618 1619 1620 1623 1630 1631 1631 1634 1647 1655 1656 1657 1659 1660 1663 1666 1666 1667 1672 1673 1682 1691 1709 1712 1714 1715 1716 1717 1721 1723 1723 1725 1725 1730 1732 1732 1748 1749 1749 1749 1750 1759 1759 1767 1771 1772 1775 1778 1779 1780 1783 1784 1786 1788 1794 1794 1794 1794 1795 1806 1819 1828 1829 1830 1836 1836 1846 1849 1853 1856 1861 1863 1863 1863 1864 1872 1874 1877 1877 1878 1885 1888 1893 1893 1895 1895 1896 1899 1907 1907 1909 1915 1918 1920 1922 1925 1931 1941 1942 1942 1943 1944 1945 1950 1958 1964 1966 1977 1978 1984 1988 1991 1991 1992 1993 2000 2003 2008 2009 2019 2019 2021 2023 2024 2026 2030 2033 2035 2035 2045 2046 2046 2048 2054 2056 2056 2057 2059 2065 2071 2072 2073 2074 2078 2081 2087 2090 2092 2094 2103 2106 2121 2122 2123 2125 2131 2131 2138 2147 2147 2148 2149 2150 2154 2156 2160 2160 2161 2171 2174 2176 2177 2182 2185 2185 2186 2187 2193 2193 2193 2194 2196 2202 2205 2209 2215 2218 2219 2225 2246 2252 2253 2256 2262 2266 2269 2275 2277 2278 2278 2278 2284 2285 2286 2286 2289 2294 2295 2297 2300 2310 2311 2311 2315 2317 2321 2322 2323 2324 2324 2333 2340 2340 2346 2348 2349 2350 2365 2368 2377 2379 2381 2384 2390 2393 2397 2398 2399 2400 2406 2412 2414 2415 2415 2417 2423 2425 2425 2426 2436 2436 2438 2441 2445 2447 2448 2450 2452 2452 2462 2463 2468 2471 2478 2479 2480 2480 2483 2487 2493 2494 2505 2507 2513 2521 2526 2527 2528 2529 2529 2530 2540 2546 2549 2551 2553 2556 2562 2564 2564 2572 2575 2576 2576 2578 2578 2583 2586 2593 2594 2594 2597 2599 2607 2608 2608 2608 2610 2615 2618 2622 2625 2635 2635 2641 2642 2643 2652 2665 2676 2677 2677 2677 2677 2683 2685 2687 2688 2691 2692 2693 2696 2699 2700 2704 2712 2712 2721 2722 2722 2722 2723 2739 2739 2741 2746 2746 2748 2748 2750 2754 2755 2756 2757 2759 2762 2780 2789 2798 2799 2804 2805 2805 2808 2811 2812 2814 2815 2816 2824 2837 2840 2840 2841 2848 2851 2852 2853 2855 2860 2861 2869 2869 2869 2870 2875 2876 2877 2883 2885 2887 2888 2893 2895 2909 2911 2911 2911 2912 2914 2917 2929 2939 2940 2942 2944 2952 2955 2955 2956 2961 2969 2974 2974 2979 2984 2985 2986 2988 2988 2988 2997 2998 3008 3009 3014 3016 3016 3016 3016 3023 3024 3024 3024 3026 3032 3040 3040 3043 3043 3049 3057 3058 3059 3070 3071 3075 3084 3087 3089 3092 3099 3102 3103 3107 3111 3112 3113 3114 3114 3116 3121 3122 3128 3129 3139 3144 3147 3153 3154 3155 3158 3163 3163 3171 3171 3172 3177 3179 3180 3180 3187 3187 3203 3204 3206 3214 3215 3220 3222 3225 3226 3231 3233 3234 3236 3242 3242 3242 3243 3249 3250 3261 3268 3274 3275 3277 3285 3286 3286 3291 3291 3291 3291 3302 3302 3303 3308 3310 3310 3311 3316 3318 3319 3327 3340 3343 3346 3348 3350 3350 3351 3351 3355 3373 3378 3378 3380 3388 3389 3390 3390 3398 3405 3405 3405 3406 3408 3414 3415 3416 3417 3421 3422 3431 3431 3431 3438 3439 3441 3447 3449 3455 3458 3461 3465 3466 3478 3480 3481 3501 3502 3503 3503 3504 3506 3506 3509 3511 3518 3518 3519 3520 3520 3523 3529 3534 3537 3543 3544 3545 3546 3549 3561 3562 3569 3573 3577 3578 3578 3578 3580 3586 3586 3589 3595 3602 3608 3609 3616 3619 3632 3634 3635 3637 3642 3643 3644 3647 3647 3648 3648 3649 3652 3657 3657 3665 3666 3668 3674 3676 3680 3687 3690 3690 3691 3692 3693 3701 3706 3708 3709 3717 3725 3733 3733 3736 3739 3756 3758 3758 3762 3762 3763 3770 3772 3776 3778 3779 3779 3779 3788 3793 3794 3796 3797 3803 3804 3805 3805 3807 3813 3815 3815 3820 3821 3827 3837 3840 3843 3846 3848 3850 3853 3862 3864 3867 3871 3872 3876 3880 3881 3886 3902 3906 3907 3907 3909 3909 3910 3914 3917 3918 3919 3925 3928 3933 3933 3934 3935 3935 3942 3942 3943 3944 3951 3957 3968 3968 3974 3977 3977 3977 3978 3981 3984 3985 3990 3995 3996 3999 4004 4009 4009 4034 4038 4038 4042 4045 4049 4049 4056 4056 4056 4061 4062 4063 4064 4065 4065 4066 4070 4071 4072 4072 4080 4080 4089 4090 4099 4105 4105 4105 4109 4109 4113 4118 4122 4124 4124 4140 4140 4146 4159 4162 4171 4173 4173 4177 4177 4179 4184 4184 4185 4193 4193 4194 4195 4195 4196 4196 4201 4202 4203 4209 4212 4212 4212 4219 4220 4227 4233 4237 4242 4242 4244 4253 4253 4255 4256 4272 4272 4277 4287 4287 4299 4301 4308 4308 4308 4315 4315 4324 4324 4324 4324 4334 4334 4340 4340 4340 4340 4342 4343 4343 4343 4343 4343 4356 4356 4356 4357 4357 4358 4358 4358 4368 4370 4372 4384 4400 4400 4400 4414 4414 4471"))
    print("-".join(LeaderboardCyclopeptideSequencing("0 71 113 129 147 200 218 260 313 331 347 389 460", 10)))
