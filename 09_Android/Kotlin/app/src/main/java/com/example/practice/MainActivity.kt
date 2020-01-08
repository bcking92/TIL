package com.example.practice

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.room.Room

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val lotto = mutableListOf<Int>(-1,-1,-1,-1,-1,-1)
        val recommended_nums = findViewById<TextView>(R.id.recommended_nums)
        val btn_recommendation = findViewById<Button>(R.id.btn_recommendation)
        recommended_nums.setText(lotto.toString())

        val db = Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java, "database-name"
        ).build()
    }

    /** Called when the user taps the Send button */
    fun recommendationNumber() {
        // Do something in response to button
    }
}
