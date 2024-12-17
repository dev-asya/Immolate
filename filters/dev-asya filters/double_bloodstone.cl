// Searches for any seed with 2 Bloodstone Jokers early ish. (For practice writing filters)


#include "lib/immolate.cl"
long filter(instance* inst) {
    int score = 0;
    next_pack(inst, 0); //the first pack will always be a Buffoon Pack
    for (int packIndex = 1; packIndex <= 7; packIndex++) {
        pack _pack = pack_info(next_pack(inst, 1));
        item cards[5];
        if (_pack.type == Buffoon_Pack) {
           buffoon_pack(cards, _pack.size, inst, 1);
        } else continue;
        
        for (int i = 0; i < _pack.size; i++) {
            if (cards[i] == Bloodstone) {
                score++;
            }
        }
    }
    return score;
}