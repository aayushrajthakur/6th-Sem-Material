package com.example.myrecycler;

public class Items {
    String NameView;
    String DescView;
    int imageview;

    public Items(String nameView, String descView, int imageview) {
        NameView = nameView;
        DescView = descView;
        this.imageview = imageview;
    }

    public int getImageview() {
        return imageview;
    }

    public void setImageview(int imageview) {
        this.imageview = imageview;
    }

    public String getDescView() {
        return DescView;
    }

    public void setDescView(String descView) {
        DescView = descView;
    }

    public String getNameView() {
        return NameView;
    }

    public void setNameView(String nameView) {
        NameView = nameView;
    }
}
