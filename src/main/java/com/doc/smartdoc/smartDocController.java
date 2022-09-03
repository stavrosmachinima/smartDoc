package com.doc.smartdoc;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class smartDocController {

    @GetMapping("/")
    public String giveHome(Model model){
        model.addAttribute("exams",new Exams());
        return "query.html";
    }

    @PostMapping("/process")
    public String processData(Exams exams)
    {
        System.out.println(exams);
        transform(exams);
        System.out.println(exams);
        return "query.html";
    }

    private void transform(Exams exams){
        if (exams.getAge()==2)
            exams.setAge(0);
        exams.setRestecg(exams.getRestecg()-1);
        exams.setExang(exams.getExang()-1);
        exams.setCa(exams.getCa()-1);
    }
}
