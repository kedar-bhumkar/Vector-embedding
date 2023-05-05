import { Component } from '@angular/core';
import { WebserviceService } from './webservice.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  prompt: String = '';
  response: String = '';
  loading:boolean = false

  constructor(private webService: WebserviceService) {}

  ngOnInit(): void {}

  getResponse() {
    //this.response = 'Hatim tai';
    this.loading = true;
    this.webService.getChatData(this.prompt).subscribe((payload) => {
      console.log('response - ' + JSON.stringify(payload));
      this.loading = false;
      this.response = payload.reply;

    });
  }
  clearResponse() {
    this.response = '';
    this.prompt = '';
  }
}
