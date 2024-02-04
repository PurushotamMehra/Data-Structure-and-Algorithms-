public class CamelCaseConverter {
    public static void main(String[] args) {
        String inputStr = "helloIndiaMan";
        camelCase(inputStr);
    }

    public static void camelCase(String string) {
        StringBuilder stringMod = new StringBuilder();
        int i = 0;
        while (i < string.length()) {
            if ('a' <= string.charAt(i) && string.charAt(i) <= 'z') {
                stringMod.append(Character.toUpperCase(string.charAt(i)));
            } else if ('A' <= string.charAt(i) && string.charAt(i) <= 'Z') {
                System.out.println(stringMod);
                stringMod = new StringBuilder();
                stringMod.append(Character.toLowerCase(string.charAt(i)));
            } else {
                stringMod.append(string.charAt(i));
            }
            i++;
        }

        System.out.println(stringMod);
    }
}