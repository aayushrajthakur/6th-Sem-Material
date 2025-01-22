package com.example.myrecycler;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class MyViewHolder extends RecyclerView.ViewHolder {
    ImageView imageView;
    TextView NameView,DescView;
    public MyViewHolder(@NonNull View itemView) {
        super(itemView);
        imageView=itemView.findViewById(R.id.myimage);
        NameView=itemView.findViewById(R.id.mynameview);
        DescView=itemView.findViewById(R.id.mydescview);
    }
}
