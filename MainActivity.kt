package com.estilstare.fxai

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            EstilStareApp()
        }
    }
}

@Composable
fun EstilStareApp() {
    var inputText by remember { mutableStateOf("") }
    var responseText by remember { 
        mutableStateOf("ሰላም! እኔ Estil Stare ነኝ። በድምፅ ወይም በጽሁፍ ማዘዝ ይችላሉ።\nHello! I am Estil Stare. You can command via voice or text.") 
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "Estil Stare - FX AI Assistant", 
            style = MaterialTheme.typography.headlineMedium
        )
        Spacer(modifier = Modifier.height(16.dp))

        Card(
            modifier = Modifier.fillMaxWidth()
        ) {
            Text(
                text = responseText,
                modifier = Modifier.padding(16.dp),
                style = MaterialTheme.typography.bodyLarge
            )
        }

        Spacer(modifier = Modifier.height(16.dp))

        OutlinedTextField(
            value = inputText,
            onValueChange = { inputText = it },
            label = { Text("ትዕዛዝ ይጻፉ / Enter command") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(8.dp))

        Button(
            onClick = {
                responseText = "ትዕዛዝ ተቀብሏል (Processed): '$inputText'. Accessibility & MT5 integration pending explicit approval."
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("ትዕዛዝ ላክ / Submit Command")
        }
    }
}
