import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        List<Integer> arr = new ArrayList<>();
        Map<String, Integer> genre = new HashMap<>(); // 각 장르별 총 재생 횟수
        Map<String, Map<Integer, Integer>> music = new HashMap<>(); // 각 장르에 속하는 노래 및 재생 횟수
        for (int i = 0; i < plays.length; i++) {
            if (!genre.containsKey(genres[i])) {
                Map<Integer, Integer> map = new HashMap<>();
                map.put(i, plays[i]);
                music.put(genres[i], map);
                genre.put(genres[i], plays[i]);
            } else {
                music.get(genres[i]).put(i, plays[i]);
                genre.put(genres[i], genre.get(genres[i]) + plays[i]);
            }
        }
        
        List<String> keySet = new ArrayList(genre.keySet());
        Collections.sort(keySet, (k1, k2) -> genre.get(k2) - genre.get(k1));
        for (String key : keySet) {
            Map<Integer, Integer> map = music.get(key);
            List<Integer> genre_key = new ArrayList(map.keySet());
            
            Collections.sort(genre_key, (s1, s2) -> map.get(s2) - map.get(s1));
            
            arr.add(genre_key.get(0));
            if (genre_key.size() > 1) {
                arr.add(genre_key.get(1));
            }
        }
        
        answer = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}