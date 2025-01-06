import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        ArrayList<String> cache = new ArrayList<>();
        
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        
        for (int i = 0; i < cities.length; i++) {
            String city = cities[i].toUpperCase(); // 대소문자 구분 안하기 위해서
            if (cache.contains(city)) { // 캐시에 city가 있다면
                cache.remove(city); // city 지우고
                cache.add(city); // 맨 뒤에 다시 추가
                answer += 1;
            }
            
            else { // 캐시에 city가 없다면
                if (cache.size() == cacheSize) { // 캐시 꽉차있으면
                    cache.remove(0); // 맨 처음 들어온(가장 적게 사용된) 도시 지우기
                    cache.add(city);
                    answer += 5;
                }
                else { // 캐시가 여유 있으면
                    cache.add(city);
                    answer += 5;
                }
            }
        }
        
        return answer;
    }
}