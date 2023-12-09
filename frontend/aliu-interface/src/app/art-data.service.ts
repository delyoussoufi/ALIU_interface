import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ArtDataService {
  private apiUrl = 'http://127.0.0.1:5000'; // Your API URL

  constructor(private http: HttpClient) { }

  searchArtObjects(query: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/artobjects`, { params: { query } });
  }
}