#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define IS_DIGIT(c) '0' <= c && c <= '9'
#define lli long long int
#define THEORTICAL_LEN 68546400
#define MAX_UNIQUE 150
const int CHR_H[] = {2636400, 101400, 3900, 150};

// Config here
const char* dataset_path = "data/hh102/hh102.rawdata.txt";
const char* datasetID = "hh102";

lli hash(char* s) {
    lli r = 0;
    int prt = 0, sid, i;
    while (s[prt] > '9') prt++;
    for (i = 0; i < prt; i++) r += (s[i] - 'A' + 1) * CHR_H[i];
    r += atoi(s + prt);
    return r;
}

void de(char* buff, lli h) {
    char tbuff[5];
    int ind = 0, v;
    while (h > CHR_H[3]) {
        v = h / CHR_H[ind];
        tbuff[ind] = v + 'A' - 1;
        h = h % CHR_H[ind++];
    }
    tbuff[ind] = '\0';
    
    sprintf(buff, "%s%03lld", tbuff, h);
}

struct Hashmap {
    int len, value[THEORTICAL_LEN], vallen[MAX_UNIQUE];
} hashmap;

void initHash(struct Hashmap* hm) {
    hm->len = 0;
    memset(hm->value, 0, sizeof hm->value);
}

void set(struct Hashmap* hm, char* key, int value) {
    lli l = hash(key);
    if (hm->value[l] == 0) hm->vallen[hm->len++] = l;
    hm->value[l] = value + 1;
}

int stringToNumeric(char* s) {
    if (IS_DIGIT(s[0])) {
        return atoi(s);
    } else {
        int l = strlen(s);
        if (l % 2 == 0) return 1;
        return 0;
    }
}

int toIndex(int y, int m, int d) {
    return (y - 2011) * 36 + (m - 1) * 3 + (int) (d / 10);
}

int main() {
    initHash(&hashmap);
    FILE* ptr = fopen(dataset_path, "r");
    if (ptr == NULL) {
        printf("File not found...");
        return -1;
    }

    int y, m , d, h, min, lastHash = -1, newHash, val;
    int c = 0;
    FILE *fptr = NULL;
    float s;
    char nameBuff[8], valueBuff[5], buff[50], outputPath[50], tempBuff[32];
    while (fscanf(ptr, "%d-%d-%d %d:%d:%f %s %s %s %s %s\n", &y, &m, &d, &h, &min, &s, nameBuff, 
                    tempBuff, buff, valueBuff, buff) == 11) {
        // de(buff, hash(nameBuff));
        if ((newHash = toIndex(y, m, d)) != lastHash) {
            // if (c > 52) break;
            lastHash = newHash;
            if (fptr != NULL) fclose(fptr);
            sprintf(outputPath, "segments/%d/%s_%d.txt", y, datasetID, newHash);
            fptr = fopen(outputPath, "w");
            c++;
            // fprintf(fptr, "%d\n", hashmap.len);
            for (int i = 0; i < hashmap.len; i++)
            {
                char tmp[20];
                de(tmp, hashmap.vallen[i]);
                fprintf(fptr, "i %s %d\n", tmp, hashmap.value[hashmap.vallen[i]] - 1);
            }
        }
        val = stringToNumeric(valueBuff);
        set(&hashmap, nameBuff, val);
        fprintf(fptr, "%d-%02d-%02d %02d:%02d:%f %s %d\n", y, m, d, h, min, s, nameBuff, val);
    }
    printf("Successfully split into %d segments\n", c);

    // Close the file
    fclose(fptr);
    return 0;
}