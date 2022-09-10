package com.doc.smartdoc;

public class Exams {

    private Boolean result;
    private Integer age;
    private int sex;
    private int chestPain;
    private Integer bloodPressure;
    private Integer cholesterol;
    // einai panw apo 120?? gia afto Boolean
    private Boolean bloodSugar;
    private int restecg;
    private Integer heartRate;
    private int exang;
    private Double oldPeak;
    private int slope;
    private int ca;
    private int thal;

    public void destroy(){
         this.age=null;
         this.sex=0;
         this.chestPain=0;
         this.bloodPressure=null;
         this.cholesterol=null;
         this.bloodSugar=null;
         this.restecg=0;
         this.heartRate=null;
         this.exang=0;
         this.oldPeak=null;
         this.slope=0;
         this.ca=0;
         this.thal=0;
    }

    @Override
    public String toString() {
        return '{' +
                "'age':" + age +
                ", 'sex':" + sex +
                ", 'chestPain':" + chestPain +
                ", 'bloodPressure':" + bloodPressure +
                ", 'cholesterol':" + cholesterol +
                ", 'bloodSugar':" + bloodSugar +
                ", 'restecg':" + restecg +
                ", 'heartRate':" + heartRate +
                ", 'exang':" + exang +
                ", 'oldPeak':" + oldPeak +
                ", 'slope':" + slope +
                ", 'ca':" + ca +
                ", 'thal':" + thal +
                '}';
    }

    public Boolean isResult() {
        return result;
    }

    public void setResult(Boolean result) {
        this.result = result;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public int getSex() {
        return sex;
    }

    public void setSex(int sex) {
        this.sex = sex;
    }

    public int getChestPain() {
        return chestPain;
    }

    public void setChestPain(int chestPain) {
        this.chestPain = chestPain;
    }

    public Integer getBloodPressure() {
        return bloodPressure;
    }

    public void setBloodPressure(Integer bloodPressure) {
        this.bloodPressure = bloodPressure;
    }

    public Integer getCholesterol() {
        return cholesterol;
    }

    public void setCholesterol(Integer cholesterol) {
        this.cholesterol = cholesterol;
    }

    public Boolean getBloodSugar() {
        return bloodSugar;
    }

    public void setBloodSugar(Boolean bloodSugar) {
        this.bloodSugar = bloodSugar;
    }

    public int getRestecg() {
        return restecg;
    }

    public void setRestecg(int restecg) {
        this.restecg = restecg;
    }

    public Integer getHeartRate() {
        return heartRate;
    }

    public void setHeartRate(Integer heartRate) {
        this.heartRate = heartRate;
    }

    public int getExang() {
        return exang;
    }

    public void setExang(int exang) {
        this.exang = exang;
    }

    public Double getOldPeak() {
        return oldPeak;
    }

    public void setOldPeak(Double oldPeak) {
        this.oldPeak = oldPeak;
    }

    public int getSlope() {
        return slope;
    }

    public void setSlope(int slope) {
        this.slope = slope;
    }

    public int getCa() {
        return ca;
    }

    public void setCa(int ca) {
        this.ca = ca;
    }

    public int getThal() {
        return thal;
    }

    public void setThal(int thal) {
        this.thal = thal;
    }
}
