typedef struct {
    int x, y, mask, e, steps;
} Info;

int minMoves(char** classroom, int classroomSize, int energy) {
    static const int dx[4] = {0, 1, 0, -1};
    static const int dy[4] = {1, 0, -1, 0};

    int m = classroomSize;
    int n = (int)strlen(classroom[0]);

    int sx = 0, sy = 0, cnt = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (classroom[i][j] == 'S') {
                sx = i;
                sy = j;
            } else if (classroom[i][j] == 'L') {
                cnt++;
            }
        }
    }

    int totalStates = 1 << cnt;

    int* id = calloc(m * n, sizeof(int));
    {
        int c = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (classroom[i][j] == 'L') {
                    id[i * n + j] = 1 << c++;
                }
            }
        }
    }

    int totalEntries = m * n * totalStates;
    int* bestEnergy = malloc(totalEntries * sizeof(int));
    memset(bestEnergy, -1, totalEntries * sizeof(int));

    bestEnergy[sx * n * totalStates + sy * totalStates + 0] = energy;

    int qCap = 4096;
    Info* q = malloc(qCap * sizeof(Info));
    int qHead = 0, qTail = 0;

    q[qTail++] = (Info){sx, sy, 0, energy, 0};

    while (qHead < qTail) {
        Info t = q[qHead++];

        if (t.mask == totalStates - 1) {
            free(id);
            free(bestEnergy);
            free(q);
            return t.steps;
        }

        if (t.e == 0) {
            continue;
        }

        for (int i = 0; i < 4; i++) {
            int nx = t.x + dx[i];
            int ny = t.y + dy[i];

            if (nx < 0 || nx >= m || ny < 0 || ny >= n ||
                classroom[nx][ny] == 'X') {
                continue;
            }

            int ne = classroom[nx][ny] == 'R' ? energy : t.e - 1;
            int nmask = t.mask | id[nx * n + ny];
            int idx = ((nx * n) + ny) * totalStates + nmask;

            if (ne > bestEnergy[idx]) {
                bestEnergy[idx] = ne;
                if (qTail >= qCap) {
                    qCap *= 2;
                    q = realloc(q, qCap * sizeof(Info));
                }
                q[qTail++] = (Info){nx, ny, nmask, ne, t.steps + 1};
            }
        }
    }

    free(id);
    free(bestEnergy);
    free(q);

    return -1;
}
