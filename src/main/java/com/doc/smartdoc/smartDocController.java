package com.doc.smartdoc;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.io.*;
import java.util.List;
import java.util.stream.Collectors;

@Controller
public class smartDocController {

    @GetMapping("/")
    public String giveHome(Model model){
        model.addAttribute("exams",new Exams());
        return "query.html";
    }

    @PostMapping("/process")
    public String processData(Exams exams) throws IOException, InterruptedException {
        //System.out.println("Old:"+exams);
        transform(exams);
        System.out.println("Transformed:"+exams);
        FileWriter myWriter=new FileWriter("src/main/resources/static/python/parameters.txt");
        myWriter.write(exams.toString());
        myWriter.close();
        System.out.println("Successfully written to file");
        boolean prediction=predict();
         return "query.html";
    }

    private boolean predict() throws IOException, InterruptedException {
        ProcessBuilder processBuilder=new ProcessBuilder("python3","src/main/resources/static/python/model.py");
        processBuilder.redirectErrorStream(true);

        Process process=processBuilder.start();
        BufferedReader results=new BufferedReader(new InputStreamReader(process.getInputStream()));
        String prediction=results.lines().collect(Collectors.joining());
        int exitCode=process.waitFor();
        System.out.println("ExitCode:"+exitCode);
        System.out.println("Prediction:"+prediction);
        return "1".equals(prediction);
    }

    private void transform(Exams exams){
        if (exams.getAge()==2)
            exams.setAge(0);
        exams.setRestecg(exams.getRestecg()-1);
        exams.setExang(exams.getExang()-1);
        exams.setCa(exams.getCa()-1);
    }
}
