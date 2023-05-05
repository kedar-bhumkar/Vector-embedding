import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class WebserviceService {
  private payloadUrl = 'http://127.0.0.1:5000/chat';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };
  constructor(private http: HttpClient) {}

  getChatData(question: String): Observable<any> {
    console.log('Inside getChatData.....');

    return this.http.post<any>(this.payloadUrl, {
      prompt: question,
    });
    //return of('Dummy')
  }
}
