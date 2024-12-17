// Seeds containing Pareidolia, Midas Mask, and Vampire in the first 2 antes.
#include "lib/immolate.cl"
long filter(instance* inst) {
    long passedFilters = 0;

    // Pareidolia ante 1
    item jkr1 = shop_joker(inst, 1);
    item jkr2 = shop_joker(inst, 1);
    if (jkr1 == Pareidolia || jkr2 == Pareidolia) passedFilters++;
    else return passedFilters;

    // Midas Mask next shop
    jkr1 = shop_joker(inst, 1);
    jkr2 = shop_joker(inst, 1);
    if (jkr1 == Midas_Mask || jkr2 == Midas_Mask) passedFilters++;
    else return passedFilters;

    // Vampire ante 2
    shop_joker(inst, 2); //This part is after the boss, which is too early
    shop_joker(inst, 2);
    jkr1 = shop_joker(inst, 2);
    jkr2 = shop_joker(inst, 2);
    if (jkr1 == Vampire || jkr2 == Vampire) passedFilters++;
    else return passedFilters;

    return 999;
}