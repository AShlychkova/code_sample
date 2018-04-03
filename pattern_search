//Шлычкова Александра 699
//Найти позиции всех вхождений шаблона в тексте длины n.

#include <iostream>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <vector>

using namespace std;

class BohrVertex{ //вершина бора
public:
    int next_vertex[26];//номера вершин, в которые попадают по итому символу
    vector <int> str_num;
    int flag; //индикатор того, что вершина является исходной строкой (а заодно подсчет количества вхождений этих строк в текст)
    char ch; // символ на ребре, ведущем в эту вершину
    int suff_link;
    int move[26]; // запоминание перехода автомата
    int parent;
    int good_suff_link;
    
    BohrVertex (int p, char c){
        fill(next_vertex, next_vertex + sizeof(next_vertex), 255);
        fill(move, move + sizeof(move), 255);
        flag = 0;
        parent = p;
        ch = c;
        suff_link = -1;
        good_suff_link = -1;
    }
};

class Bohr{
private:
    vector<BohrVertex> bohr; //вершины бора
    vector <int> pos_of_pattern; //позиции начала подсторок без вопросов в шаблоне
    vector <int> lengths_of_pattern; //длины подстрок без вопросов в шаблоне

    
    int get_suff_link(int v){ //получение суффиксной ссылки
        if(bohr[v].suff_link == -1){
            if(v == 0 || bohr[v].parent == 0){
                bohr[v].suff_link = 0;
            } else{
                bohr[v].suff_link = get_move(get_suff_link(bohr[v].parent), bohr[v].ch);
            }
        }
        return bohr[v].suff_link;
    }
    
    int get_move(int v, char c){
        if(bohr[v].move[c] == -1){
            if(bohr[v].next_vertex[c] != -1){
                bohr[v].move[c] = bohr[v].next_vertex[c];
            }
            else{
                if (v == 0){
                    bohr[v].move[c] = 0;
                } else{
                    bohr[v].move[c] = get_move(get_suff_link(v), c);
                }
            }
        }
        return bohr[v].move[c];
    }
    
    //получение сжатой суффиксной ссылки
    //Если в вершине полученной по суф. ссылке flag > 0, то это и есть искомая вершина, в ином случае рекурсивно запускаемся от этой вершины
    int get_good_suff_link(int v){ //получение сжатой суффиксной ссылки
        if(bohr[v].good_suff_link == -1){
            int u = get_suff_link(v);
            if(u == 0){
                bohr[v].good_suff_link = 0;
            }
            else{
                bohr[v].good_suff_link = (bohr[u].flag)? u:get_good_suff_link(u);
            }
        }
        return bohr[v].good_suff_link;
    }
    
    // переход по хорошим суффиксным ссылкам
    void check(int v, int k, vector <int> &vec){
        for(int  u = v; u != 0; u = get_good_suff_link(u)){
            for (int i =0; i< bohr[u].flag; ++i){
                //для всевозможных подстрок если подстрока без вопросов заканцивается в данном символе, то увеличиваем счетчик позиции, где могла бы начинаться подстрока puttern
                int j = bohr[u].str_num[i];
                int position_of_begining_of_str = k - lengths_of_pattern[j]-pos_of_pattern[j];
                if(position_of_begining_of_str >= 0){
                    vec[position_of_begining_of_str]++;
                }
            }
        }
    }
    
    

    
public:
    Bohr(){ //изначально в дереве только корневая вершина
        bohr.push_back( BohrVertex(0, -1));
    }
    
    int AddToBohr(string &s){ // добавзение подстрок шаблона в бор
        int n = 0, p = 0, i = 0, count = 0;
        for(char ch: s){
            if (ch != '?'){
                //если текущий символ не вопрос то если подстрока уже есть в боре переходим на соответствующую вершину, иначе создаем новую
                if(bohr[n].next_vertex[ch-'a'] == -1){
                    bohr.push_back(BohrVertex(n, ch-'a'));
                    bohr[n].next_vertex[ch-'a']=bohr.size()-1;
                }
                n = bohr[n].next_vertex[ch-'a'];
                ++p;
            } else if(p != 0){ //если подстрока без вопросов закончилась, запоминаем ее параметры
                bohr[n].flag++;
                bohr[n].str_num.push_back(count);
                count++;
                pos_of_pattern.push_back(i-p);
                 lengths_of_pattern.push_back(p);
                p = 0;
                n = 0;
            }
            ++i;
            
        }
        if(p != 0){
            bohr[n].flag++;
            bohr[n].str_num.push_back(count);
             lengths_of_pattern.push_back(p);
            count++;
            pos_of_pattern.push_back(i-p);
            
        }
        return count;
    }
    
    void FindAllPos(string& s, vector <int> &vec){
        int u = 0;
        for(int i = 0; i < s.length(); i++){
            u = get_move(u, s[i]-'a');
            check(u, i+1, vec);
        }
    }
    
};

int main (void){
    Bohr B;
    string a, c;
    cin>>a>>c;
    if(a.length()<=c.length()){
        vector <int> vec(c.length());
        int count = 0;
        count = B.AddToBohr(a);
        B.FindAllPos(c, vec);
        for (int i =0; i<=c.length()-a.length(); ++i){
            if (vec[i] == count){
                cout<<i<<endl;
            }
        }
    }
    return 0;
}
